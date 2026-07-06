# 7. Idempotency Keys — Deep Dive

Why every mutating money operation carries an idempotency key, what breaks without
one, and how the two-layer enforcement guarantees an **exactly-once effect** over an
unreliable network.

## 7.1 The core problem: the network is unreliable, and money ops aren't safe to repeat

When a client calls `POST /debit {amount: 2000}`, three things happen in sequence:

1. The request travels to the server.
2. The server applies the debit and commits it.
3. The response travels back to the client.

A failure can happen at **any** of these steps, and the critical insight is: **when
the client gets a timeout or a dropped connection, it cannot tell which step
failed.**

```
Client                    Server
  |  POST /debit 2000        |
  |------------------------->|
  |                          | ✅ debit committed, balance now 45050
  |         response         |
  |     X----timeout---------|   <-- response lost in the network
  |                          |
  |  "Did that work??"       |
```

A timeout is **ambiguous**. Two completely different realities produce the
*identical* symptom:

- **Reality A:** the request never reached the server. The debit did *not* happen.
- **Reality B:** the debit committed successfully, but the response was lost on the
  way back.

The client has no way to distinguish A from B.

## 7.2 The client is forced to retry — and that's the trap

The safe, standard behavior for any distributed client facing a timeout is to
**retry**. It has to — in Reality A, not retrying means the user's legitimate debit
silently vanished. So retries are non-negotiable.

But watch what a retry does in each reality **without** an idempotency key:

| | Reality A (first attempt failed) | Reality B (first attempt succeeded, response lost) |
|---|---|---|
| Client retries | Server applies debit once ✅ | Server applies debit **again** ❌ |
| Final effect | Correct: −2000 | **Wrong: −4000, double charge** |

Without an idempotency key, the server treats the retry as a brand-new, unrelated
request. In Reality B the customer is debited twice for one intended operation — a
real financial loss, and a reconciliation nightmare, because the ledger now holds two
legitimate-looking debit entries with no way to know one was a phantom.

## 7.3 Why you can't fix this any other way

You might think "just check whether a matching transaction already exists." But *what*
would you match on?

- **Amount + accounts?** Two genuine \$20 debits to the same coffee shop five minutes
  apart are legitimate and must both apply. You can't tell them apart from a retry.
- **Timestamp?** Retries can arrive seconds or minutes later, and clocks drift.

There is no intrinsic property of the request that distinguishes "the same operation
retried" from "a new, coincidentally-identical operation." **That distinction only
exists in the client's intent** — and the idempotency key is how the client
communicates it.

## 7.4 How the key fixes it

The client generates **one unique key per logical operation** (a UUID) and reuses that
*same* key on every retry of that operation:

```
POST /debit {amount: 2000}   Idempotency-Key: abc-123   <- first attempt
POST /debit {amount: 2000}   Idempotency-Key: abc-123   <- retry (same key)
```

Now the server can disambiguate:

- **Same key seen before** → "this is a retry of something I already did." Replay the
  stored original response. Do **not** apply the debit again.
- **New key** → "this is a genuinely new operation." Apply it.

This converts an **at-least-once** network (messages may be delivered multiple times)
into an **exactly-once effect** (the debit is applied exactly once, no matter how many
times the request arrives). Two genuine \$20 debits get two different keys and both
apply; ten retries of one debit share one key and apply once.

Reads (`GET /balance`) don't need a key because reading is naturally idempotent —
repeating it changes nothing. It is specifically the **state-mutating money
operations** that require it.

## 7.5 Two-layer enforcement (defense in depth)

The check lives in two places, because retries can also *race* each other — a client
fires a retry while the original is still in flight.

### Layer 1 — Fast path: cheap early-out for the common duplicate

Before doing any real work, the service tries to "claim" the idempotency key with a
**conditional write**: *only write this key if it doesn't already exist.* The
check-and-write is one atomic operation:

```
put(key = "abc-123")  IF key does not exist
```

- **Claim succeeds** → the key was new; this is the first time we've seen this
  operation. Proceed to apply the debit.
- **Claim fails** (key already present) → this is a duplicate/retry. Skip all the
  work; return the stored original response.

Why "fast path"? The overwhelmingly common duplicate is a retry arriving *after* the
original fully finished (Reality B — response lost, client retries seconds later). By
then the key is already stored, so one cheap key lookup catches it and we avoid
opening a database transaction, taking row locks, etc. It is an **early-out
optimization** for the common case.

### The race the fast path alone can't fully cover

The fast path handles a retry that arrives *after* the first request finishes. But two
copies of the same request can be **in flight simultaneously**:

- A client's HTTP library times out at 5 s and retries — but the original was just
  slow, not dead, and is still processing.
- A load balancer retries a request it thinks stalled.
- The user double-clicks "Send."

Because the service is stateless and autoscaled, the two copies can land on **two
different instances** at nearly the same moment:

```
Instance X                         Instance Y
  claim key → succeeds?              claim key → succeeds?
  ... start debit ...                ... start debit ...
```

The atomic conditional write means only one instance can *win* the claim, so a naive
"check then write" race is prevented at layer 1. But the fast path and the actual
database commit are **two separate systems, not in one transaction**, so gaps remain:

- **Instance X claims the key, then crashes** before committing the Aurora debit. The
  key is claimed but no debit happened. If we treated "key exists" as "already done,"
  a retry would wrongly skip a debit that never occurred — so the claim can't be a
  permanent "done" marker on its own, which reopens a window.
- **TTL expiry / eviction:** the key has a TTL; edge timing around expiry can let a
  late duplicate see "no key."
- **Fast-path store briefly unavailable:** we don't want to hard-fail every money
  operation, so we fall through and rely on the database — a path with no fast-path
  protection at all.

The fast path is an **optimization** that can be bypassed. Correctness must not depend
on something bypassable.

### Layer 2 — Durable backstop: the database is the final arbiter

The real guarantee lives where the debit itself commits: a
`UNIQUE(idempotency_key)` constraint on the `transactions` table, enforced **inside
the same transaction** that writes the ledger and updates the balance.

This means the same key can physically exist in the table **at most once** — not a
check we run in application code, but a rule the database enforces on the data itself.

Replay the race, now with the backstop:

```
Instance X                         Instance Y
  BEGIN                              BEGIN
  ... apply debit ...                ... apply debit ...
  INSERT transactions               INSERT transactions
    (idempotency_key='abc-123')       (idempotency_key='abc-123')
  COMMIT ✅                          COMMIT ❌ UNIQUE VIOLATION
```

Even if both instances reach commit, the database **cannot** store two rows with the
same key. One commit wins; the other is **rejected atomically**. The service catches
the unique-violation error, recognizes "someone else already did this exact
operation," and returns the winner's result instead of applying a second debit.

Because this check and the debit are in **one atomic transaction**, there is no gap to
race through — the whole thing (unique key + ledger entries + balance update) commits
together or not at all. The database is the single final arbiter; there is no separate
"check" and "act" for a race to slip between.

Even the "replay the original response" feature has a durable fallback: the
`transactions` table stores `idempotency_key → transaction_id`, so when the constraint
rejects a duplicate, the original transaction can be looked up and its response
reconstructed.

### Why both layers — the division of labor

| | Fast path | Durable backstop (`UNIQUE`) |
|---|---|---|
| **Job** | Cheaply catch the *common* duplicate (late retry) before doing expensive work | *Guarantee* no double-apply, even in a simultaneous race or when the fast path is bypassed |
| **Property** | Fast and cheap, but bypassable (TTL, crash-between-steps, store unavailable) | Absolutely correct and atomic, but only triggers at commit time (after work is done) |
| **If it's the only layer** | Can be raced/bypassed → not safe alone | Every duplicate pays full cost (opens txn, takes locks) before being rejected → wasteful |

This is the classic pattern: an **optimistic fast path for performance** backed by a
**pessimistic guarantee for correctness**.

- The fast path makes the **common** case cheap: ~99% of duplicates are late retries,
  caught by one tiny lookup — no wasted database transaction.
- The backstop makes **every** case correct: the rare simultaneous race, or a
  duplicate that slips past a crashed/expired/unavailable fast path, is still caught
  with certainty by the database's unique constraint.

Neither alone suffices. Fast path alone = fast but not guaranteed. Backstop alone =
guaranteed but every duplicate wastefully does full work before being rejected.
Together = **cheap in the common case, correct in every case.**

## 7.6 What happens if we don't use an idempotency key

1. **Double (or N-fold) charges** on any timeout+retry — the headline bug.
2. **The client is stuck in an unsafe dilemma:** retry and risk double-charging, or
   don't retry and risk silently losing legitimate operations. There is no safe
   choice.
3. **Generic retry infrastructure silently duplicates money:** load balancers, API
   gateways, and HTTP client libraries retry on 5xx/timeouts *by default*.
4. **Reconciliation can't save you:** the nightly job checks that
   `SUM(ledger) == balance`. A double debit is internally *consistent* — the balance
   correctly reflects both entries — so nothing flags it. Arithmetically it isn't
   wrong; it's just not what the user intended. The error is invisible to the safety
   net.

## 7.7 One-line mental model

> The network guarantees *at-least-once* delivery, but debiting money is not
> *idempotent* — applying it twice changes the outcome. The idempotency key is the
> bridge that lets the server recognize a retry as a retry.
>
> The fast-path check is a **doorman** who turns away most repeat visitors cheaply,
> but a doorman can be dodged. The `UNIQUE` constraint is a **turnstile that
> physically lets only one person through**, no matter how many slip past the
> doorman. You want both: the doorman keeps the line moving, the turnstile makes the
> guarantee.
