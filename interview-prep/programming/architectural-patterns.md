# Architectural Patterns

Higher-level patterns that define how the major parts of a system are organized. Unlike GoF patterns (object-level), these govern layers, data flow, and responsibilities across an entire application.

---

## Layered Architecture (N-Tier)

The most common backend structure. Each layer has a single responsibility and only communicates with the layer directly below it.

```
┌─────────────────────────┐
│   Presentation Layer    │  HTTP handlers, serialization
├─────────────────────────┤
│  Business Logic Layer   │  Domain rules, use cases, services
├─────────────────────────┤
│   Data Access Layer     │  Repositories, queries, ORM
├─────────────────────────┤
│       Database          │  Postgres, Redis, etc.
└─────────────────────────┘
```

Dependencies flow **downward**: the business logic layer imports and knows about the data access layer. This is the key limitation — swapping the database or ORM can ripple up into business logic.

```python
# Layered — business logic depends on the concrete data access class
from app.data_access.user_dao import UserDAO   # domain imports infrastructure

class UserService:
    def __init__(self):
        self.dao = UserDAO()   # coupled — can't test without a real DB
```

**Why it matters:** Enforces separation of concerns. Changing the database doesn't touch business logic; changing the API format doesn't touch data access.

**Pitfall:** "Lasagna code" — logic leaks between layers, especially when the data access layer returns ORM objects directly to the business layer, coupling both to the DB schema. See [Hexagonal Architecture](#hexagonal-architecture-ports--adapters) for how dependency inversion fixes this.

---

## MVC (Model-View-Controller)

Classic pattern for web frameworks (Django, Rails, Spring MVC). Separates data, UI, and request handling.

- **Model** — data and business logic (the domain)
- **View** — renders the response (HTML template, JSON serializer)
- **Controller** — receives the HTTP request, coordinates model and view

```
Request → Controller → Model (read/write data)
                     ↓
                    View → Response
```

**Key point:** In API backends there's often no traditional "View" — the serialized JSON response fills that role. Some frameworks call the pattern **MC** or fold it into a service layer.

### The "Model" confusion in modern backends

The word "Model" means different things depending on context:

| Term | In classic MVC | In FastAPI / modern practice |
|---|---|---|
| Model | Domain entity + business logic | Often just the Pydantic schema (request/response shape) |
| View | HTML template | JSON serialization |
| Controller | Coordinates model and view | Route handler |

The Pydantic schema is actually a **DTO (Data Transfer Object)** — it describes the wire format at the boundary, not the domain. The real "Model" is the domain entity with behavior, which lives in the service layer.

### MVC + Hexagonal

MVC and Hexagonal are not in conflict — MVC describes the flow of an HTTP request, Hexagonal describes where the domain boundary sits. When combined, the layers map like this:

```
[Pydantic DTO]         ← input validation at the boundary
      │
[Route Handler]        ← Controller = inbound adapter (HTTP → domain)
      │
[Service / Use Case]   ← Domain core (business logic)
      │
[Repository port]      ← outbound port (interface defined by the domain)
      │
[PostgresRepository]   ← outbound adapter (infrastructure detail)
      │
[Domain Entity]        ← the real Model (has behavior, not just fields)
      │
[Pydantic DTO]         ← output serialization at the boundary
```

```python
# DTO (boundary) — NOT the domain model
class CreateOrderRequest(BaseModel):
    user_id: int
    item_ids: list[int]

class OrderResponse(BaseModel):
    id: int
    total: float

# Domain entity (the real Model — has behavior)
class Order:
    def __init__(self, user_id: int, items: list):
        self.id = None
        self.user_id = user_id
        self.items = items

    def total(self) -> float:
        return sum(i.price for i in self.items)

# Service (domain core — business logic lives here, not in the controller)
class OrderService:
    def __init__(self, repo: OrderRepository):
        self._repo = repo

    def create_order(self, user_id: int, item_ids: list[int]) -> Order:
        items = self._repo.get_items(item_ids)
        order = Order(user_id, items)
        self._repo.save(order)
        return order

# Controller (inbound adapter — thin, no business logic)
@app.post("/orders", response_model=OrderResponse)
def create_order(body: CreateOrderRequest, service: OrderService = Depends()):
    order = service.create_order(body.user_id, body.item_ids)
    return OrderResponse(id=order.id, total=order.total())
```

Adding a service layer and repositories doesn't stop being MVC — the Controller is still the route handler and the Model is still the domain. What changes is the Model is no longer the Pydantic schema; it's the domain entity and service at the center of the hexagon.

---

## MVP (Model-View-Presenter)

Variant of MVC where the **Presenter** owns all the UI logic and the View is completely passive (just displays what it's told). The View and Model never communicate directly.

```
View ←→ Presenter ←→ Model
```

More common in desktop/mobile UIs than REST APIs, but the principle (passive view, logic in presenter) appears in frontend frameworks and testable UI components.

---

## Hexagonal Architecture (Ports & Adapters)

The domain (business logic) sits at the center and knows nothing about the outside world. External systems — HTTP, databases, message queues — connect via **adapters** that implement **ports** (interfaces defined by the domain).

```
         [ HTTP Adapter ]
               │
[ CLI ] ── [ Domain Core ] ── [ DB Adapter ]
               │
       [ Message Queue Adapter ]
```

**Port** = an interface the domain defines (e.g., `UserRepository`, `EmailSender`).  
**Adapter** = the concrete implementation that talks to the real system (e.g., `PostgresUserRepository`, `SendGridEmailSender`).

```python
# Port (defined in the domain layer)
class UserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: int) -> User | None: ...

# Adapter (lives in infrastructure layer — imports domain, not the other way around)
class PostgresUserRepository(UserRepository):
    def get_by_id(self, user_id: int) -> User | None:
        row = self._db.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        return User(**row) if row else None

# In tests, swap for an in-memory adapter — no DB needed.
class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._store: dict[int, User] = {}

    def get_by_id(self, user_id: int) -> User | None:
        return self._store.get(user_id)
```

**Why it matters:** The domain is fully testable without any infrastructure. You can swap databases, HTTP frameworks, or message queues without touching business logic.

Also known as **Clean Architecture** (Robert C. Martin) or **Onion Architecture** — same idea, different naming.

### vs. Layered Architecture

Both separate business logic from infrastructure, but the key difference is **dependency direction**.

In layered, dependencies flow downward — business logic imports data access:
```
Presentation → Business Logic → Data Access → Database
```

In hexagonal, all dependencies point inward — infrastructure imports the domain, never the reverse:
```
PostgresRepo ──implements──▶ [UserRepository port] ◀── Domain
```

The domain defines the interface (port); the infrastructure implements it. The domain never imports anything from infrastructure.

```python
# Layered — business logic is coupled to the concrete DAO
from app.data_access.user_dao import UserDAO   # domain imports infrastructure

class UserService:
    def __init__(self):
        self.dao = UserDAO()   # can't test without a real DB

# Hexagonal — domain depends only on its own abstraction
class UserService:
    def __init__(self, repo: UserRepository):  # depends on the port (ABC)
        self._repo = repo                      # inject InMemoryRepo in tests

# Infrastructure imports the domain, not the reverse
from app.domain.ports import UserRepository    # infra depends on domain

class PostgresUserRepository(UserRepository):
    ...
```

The other difference is **topology**. Layered assumes a single top-to-bottom flow (HTTP → logic → DB). Hexagonal treats all external systems symmetrically — HTTP, CLI, and a queue consumer are all just inbound adapters calling the same domain core. This matters when a service has multiple entry points.

| | Layered | Hexagonal |
|---|---|---|
| Dependency direction | Each layer depends on the one below | Everything depends on the domain; domain depends on nothing |
| Business logic isolation | By convention | Enforced by dependency inversion |
| Testability | Need to mock concrete classes | Swap adapters; domain is pure |
| Entry points | One flow (HTTP → logic → DB) | Many inbound adapters, same domain core |
| Complexity | Lower — easy to start with | Higher — more interfaces and indirection |

In practice, hexagonal is layered architecture with the **Dependency Inversion Principle** applied strictly. Many teams start layered and drift toward hexagonal as the codebase grows and testing becomes painful.

---

## CQRS (Command Query Responsibility Segregation)

Separate the **write model** (commands that change state) from the **read model** (queries that return data). They can have different data shapes, different databases, and scale independently.

```
         ┌──────────┐     ┌──────────────┐
Write ──▶│ Commands │────▶│  Write Store │ (normalized, consistent)
         └──────────┘     └──────┬───────┘
                                 │ sync/event
         ┌──────────┐     ┌──────▼───────┐
Read  ◀──│ Queries  │◀────│  Read Store  │ (denormalized, fast)
         └──────────┘     └──────────────┘
```

**Simple CQRS** (same DB, separate classes):
```python
# Command side — handles writes
class CreateOrderCommand:
    def __init__(self, user_id: int, items: list):
        self.user_id = user_id
        self.items = items

class CreateOrderHandler:
    def handle(self, cmd: CreateOrderCommand) -> None:
        order = Order.create(cmd.user_id, cmd.items)
        self._repo.save(order)

# Query side — optimized reads
class OrderSummaryQuery:
    def get_user_orders(self, user_id: int) -> list[dict]:
        return self._db.execute(
            "SELECT id, total, status FROM orders WHERE user_id = %s", (user_id,)
        )
```

**When to use:** Read-heavy systems where reads and writes have different scaling needs or data shapes. Often paired with Event Sourcing.

**Tradeoff:** Adds complexity (two models to maintain, eventual consistency on the read side).

---

## Event Sourcing

Instead of storing the current state of an entity, store the **sequence of events** that led to that state. Current state is derived by replaying events.

```
Traditional:  users table → { id: 1, balance: 150 }

Event Sourced: events table →
  { AccountOpened,  amount: 100 }
  { MoneyDeposited, amount: 100 }
  { MoneyWithdrawn, amount: 50  }
  → replay → balance: 150
```

```python
from dataclasses import dataclass
from typing import Any

@dataclass
class DomainEvent:
    type: str
    data: dict

class BankAccount:
    def __init__(self):
        self.balance = 0
        self._events: list[DomainEvent] = []

    def deposit(self, amount: float) -> None:
        self._apply(DomainEvent("MoneyDeposited", {"amount": amount}))

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self._apply(DomainEvent("MoneyWithdrawn", {"amount": amount}))

    def _apply(self, event: DomainEvent) -> None:
        if event.type == "MoneyDeposited":
            self.balance += event.data["amount"]
        elif event.type == "MoneyWithdrawn":
            self.balance -= event.data["amount"]
        self._events.append(event)

    @classmethod
    def rebuild(cls, events: list[DomainEvent]) -> "BankAccount":
        account = cls()
        for event in events:
            account._apply(event)
        return account
```

**Benefits:** Full audit trail, time travel (reconstruct state at any point), event replay for new projections.

**Tradeoffs:** Querying current state requires projection/snapshot logic; schema evolution of old events is hard.

---

## Microservices

Decompose an application into small, independently deployable services, each owning its own data and communicating over a network (REST, gRPC, message queues).

```
         ┌──────────────┐     ┌──────────────┐
         │  User Service│     │ Order Service│
         │  (own DB)    │     │  (own DB)    │
         └──────┬───────┘     └──────┬───────┘
                │     API Gateway    │
                └────────┬───────────┘
                         │
                      Client
```

**When to split:** services need to scale independently, are owned by different teams, or have genuinely different deployment lifecycles.

**Key challenges:**
- **Data consistency** — no shared transactions across services; use Saga pattern or eventual consistency.
- **Network failures** — calls can fail; use circuit breakers, retries, timeouts.
- **Distributed tracing** — a single request touches many services; need correlation IDs and tracing (Jaeger, Datadog).
- **Service discovery** — how services find each other (Kubernetes DNS, Consul).

**Monolith first:** Start with a modular monolith. Extract services only when you have a clear scaling or team ownership reason — premature microservices are expensive.

---

## Summary Table

| Pattern | Level | Key Idea | When to Use |
|---|---|---|---|
| Layered (N-Tier) | App structure | Separate presentation, logic, data | Almost always — it's the baseline |
| MVC | App structure | Model, View, Controller separation | Web frameworks, REST APIs |
| Hexagonal | App structure | Domain at center, infrastructure as adapters | When testability and framework independence matter |
| CQRS | Data flow | Separate read and write models | Read-heavy systems, complex domain writes |
| Event Sourcing | Data storage | Store events, not state | Audit trails, financial systems, complex domain history |
| Microservices | Deployment | Independent services, own data | Large teams, independent scaling needs |
