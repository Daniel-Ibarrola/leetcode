# Migrating from Bash Scripts to Python

Treat this as a gradual refactor, not a big-bang rewrite.

Start by inventorying scripts, owners, and environments. 
Group them by complexity and risk, then replace low-risk helpers 
first and move inward. 
Keep the old bash scripts as a stable fallback while you port logic into Python.

### Suggested approach

1. **Inventory scripts** — document what each script does and how it runs.
2. **Wrap with Python CLI** — create a thin Python entry point that calls the bash script.
3. **Move logic incrementally** — port small pieces into Python modules.
4. **Add tests** — capture current behavior with unit and regression tests.
5. **Verify parity** — compare outputs and side effects between bash and Python.
6. **Deploy safely** — use a feature flag and keep a rollback path.
7. **Archive bash** — once Python is stable, make it the default and retire the old script.


## Questions to ask
* How are legacy scripts currently organized, documented, and maintained?
* How do you define success for this role in the first 3–6 months?
* What tools do you use for code review, testing, and deployment?
* Who are the main stakeholders I’d work with when clarifying legacy behavior?
* What are the biggest challenges the team is facing right now with this migration effort?
* How does the team balance focused development time with collaboration? For example, standups, planning, and design discussions
