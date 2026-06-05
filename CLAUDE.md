# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

This project uses [uv](https://docs.astral.sh/uv/) for dependency management and Python 3.13.

```bash
# Install dependencies
uv sync

# Run all tests
uv run pytest

# Run a single test file
uv run pytest tests/concurrency/async/test_web_crawler.py

# Run a specific test by name
uv run pytest tests/graphs/test_adjacency_list.py::test_name

# Format code
uv run black src/ tests/
```

Asyncio tests run with `asyncio_mode = auto` (set in `pytest.ini`), so no `@pytest.mark.asyncio` decorator is needed.

## Architecture

`src/leetcode/` contains solutions organized by algorithmic category. Each category is a subpackage with one file per problem or data structure. Tests mirror this layout under `tests/`.

**Categories:**
- `basic/` — array manipulation, sorting fundamentals
- `two_pointers/`, `sliding_window/` — linear scan techniques
- `prefix_sum/` — cumulative sum problems
- `problem_solving/` — hash map / set based problems (two sum, four sum count, etc.)
- `binary_tree/`, `graphs/` — tree/graph traversal and construction
- `heap/` — min/max heap implementations and k-th element problems
- `intervals/` — merge, insert, meeting room problems
- `matrix/` — 2D array manipulation (spiral, rotate, reshape)
- `stack/` — bracket matching, decode string
- `backtracking/` — word search
- `recursion/` — list flattening
- `greedy/` — gas station, cookie assignment, refuel stops
- `linked_list/` — linked list operations
- `concurrency/` — threading (`threads/`) and asyncio (`asyncio/`) examples
- `decorators/`, `refactoring/` — Python-specific exercises

**The concurrency module** is the most complex: `web_crawler.py` implements `UserProfileFetcher` with async rate limiting via `aiolimiter.AsyncLimiter`, a global `asyncio.Semaphore` for concurrency control, exponential backoff retries, and request timing metrics. The `tasks.py` module demonstrates producer/consumer patterns with `asyncio.Queue`.

**Reference material** lives outside `src/`:
- `cheatsheets/` — algorithm reference sheets (arrays, graphs, heaps, DP, etc.)
- `interview-prep/` — behavioral, system design, and language-specific Q&A
- `problems.md` — curated problem list organized by module/difficulty
