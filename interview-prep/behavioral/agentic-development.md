# Agentic development

## How do you use AI tools in your daily workflow?

I use AI as a productivity multiplier across the full development cycle—especially for accelerating analysis, generating options, and tightening feedback loops—but I keep humans accountable for design decisions and final code quality.

1) Understand the problem and constraints  
- I use AI to quickly summarize unfamiliar areas of the codebase, propose clarifying questions, and surface relevant docs/ADRs.  
- I’m careful about confidentiality (no secrets or sensitive data) and I verify any claims with source code and official documentation.

2) Produce a concrete plan before coding  
- I ask AI to turn the spec into an implementation plan: requirements, non-goals, API changes, migration/rollout strategy, risks, and a validation checklist.  
- I review and edit the plan myself to ensure it aligns with architecture, operability, and team conventions.

3) Implement in small, reviewable increments  
- I use AI to draft scaffolding, suggest edge cases, and generate test cases (unit/integration).  
- For larger tasks, I explicitly timebox the agent: “implement up to X, then stop for review” to keep changes understandable and easy to revert.

4) Validate  
- I run the full validation plan: tests, linters, type/static analysis, and targeted negative/edge-case testing.  
- If AI proposes a fix, I require it to explain the root cause and why the change is safe.

5) Review and ship  
- For high-impact changes, I’ll use a second-pass AI review to spot missed edge cases or confusing code, then I do the final human review.  
- I use AI to help draft a clear PR description (what/why/how tested/rollout/risks), but I own the final narrative and approvals.

Net: AI helps me move faster on exploration and boilerplate, while maintaining senior-level rigor on correctness, security, and maintainability.

## A feature accelerated with AI
## Debugging a CI-only Windows/MSYS2 issue with AI (and hardening the runner image)

We had a CI bug on our Windows runners (Windows containers running on GKE, based on an internal Docker image) when using
MSYS2 together with the Google Cloud CLI. Some `gcloud` commands failed when arguments contained spaces. This was painful
because it mostly surfaced in CI and was slow to iterate on.

I used AI to accelerate the investigation in a structured way: it helped me outline a debug plan (get a local repro,
narrow the scope, compare environments) and set up a Windows VM using our Windows Docker image so I could reproduce the
issue outside the full CI loop. That got me to a fast feedback cycle even though I’m not deeply specialized in Windows.

In the VM I found the key root cause: `gcloud` was installed under a path containing spaces, and under MSYS2 that led to
incorrect invocation/quoting behavior. A reliable workaround was to avoid the space-sensitive path and also invoke the
native Windows entrypoint (`gcloud.cmd`). I implemented two fixes:
- Install `gcloud` in a location without spaces inside the image.
- Provide a `gcloud` alias/wrapper that maps to `gcloud.cmd` so MSYS2 shells resolve it correctly.

When I first tried the alias approach in CI it still failed, which was confusing because it worked in an interactive
session. AI helped with the key insight: workflow steps run in non-interactive shells that don’t source profile scripts,
so aliases defined in shell profiles won’t be present. That pushed me to make the fix “image-level” rather than relying
on interactive shell initialization.

I updated the Windows runner Docker image to bake in both the installation-path fix and the `gcloud` alias/wrapper, and
rolled it out to the GKE-based runners. This eliminated the class of failures and prevented future corrupted CI runs,
while also highlighting how I use AI effectively: speed up reproduction and hypothesis generation, but validate via
controlled repros and environment differences when AI starts looping.

## Refactoring/Migration with AI

**Situation:** At a private security company, we had an internal scheduling web app with a React 
frontend that had accumulated significant technical debt. Several components had 
grown huge, mixed business logic with rendering, and used state/effects in a way that caused cascading 
re-renders. Using React DevTools/Profiler, we confirmed that some interactions triggered frequent 
re-renders and multi-second update times, and our Web Vitals showed INP in the *poor* range.

**Task:** Improve frontend performance and maintainability without doing a risky rewrite, 
while keeping changes safe to ship and easy to review.

**Action:**
- I used AI as a planning assistant to draft an incremental refactor roadmap 
(sequencing, component boundaries, and test strategy). I reviewed it critically, corrected it based on our codebase
constraints, and got manager buy-in.
- I executed the work in small phases:
  - Split oversized components into smaller, single-responsibility components.
  - Extract business logic into dedicated, testable modules and add targeted tests to create a safety net.
  - Improve codebase structure by organizing by page/feature instead of keeping everything in one `src/` directory.
- After the structure was improved, I addressed the main rendering issues. A major root cause was misuse of `useEffect` to update state in response to user events, which created extra render cycles. I moved that logic into event handlers and tightened dependencies to prevent unnecessary updates.
- For a sidebar that rendered a long employee list, profiling showed re-renders were the main cost. The rows weren’t complex enough to justify virtualization, so I used memoization/stable props to avoid recomputing and re-rendering unchanged list items.
- To de-risk the changes (especially with AI-assisted edits), I shipped the refactor via incremental PRs and regression testing, so each step was reviewable and we could catch issues early.

**Result:** The refactor made the codebase easier to understand and safer to modify, and it improved real user experience: INP moved from *poor* to *good*, and the problematic components stopped re-rendering unnecessarily (confirmed via profiling). The team also moved faster afterward because changes were smaller, better-tested, and easier to review.

## Learning an unfamiliar stack quickly with AI

In my current role supporting a team at Google, I had to ramp up quickly in a large internal tooling ecosystem.
One of the steepest learning curves was Blaze/Bazel. I used AI to accelerate onboarding: first to build a mental
model of Bazel concepts (rules/targets, providers, hermetic execution), then to propose a learning plan and exercises.
I treated AI output as hypotheses and validated everything with Bazel docs/examples, small experiments, and code review.

After ramping up, I shipped a Bazel-native integrity check to prevent releasing broken Python wheels. We built multiple
wheel variants (CPU/GPU) and also separated artifacts into a Python wheel and a C++ wheel containing `.so` libraries.
The key failure mode was: a wheel builds successfully but is missing required Python modules or shared libraries, which
only shows up after release or at runtime.

A hard requirement was hermeticity, so I wanted the check to run as `bazel test` and be enforceable in CI. I explored a
few approaches:
- External scripts to inspect wheel contents — fast to prototype, but breaks hermeticity and is hard to reproduce.
- Manually curated `filegroup`s passed into tests — hermetic, but unmaintainable as targets and dependencies evolve.

The final solution was to use a Bazel **aspect** to traverse relevant targets and collect the expected runtime files
(Python sources and `.so` libs) from the build graph. The test then compared the expected set against the actual wheel
contents, and we integrated it into CI. This made the check hermetic, scalable as the dependency graph changed, and it
prevented corrupted/incomplete wheels from being released.

AI helped most in accelerating exploration (design options, Bazel idioms, edge cases) and improving communication, while
correctness was ensured through tests, CI, and Bazel-native mechanisms rather than trusting AI output blindly.