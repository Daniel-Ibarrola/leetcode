# Design Patterns for Backend

GoF patterns most relevant to backend systems, organized by category.

---

## Creational Patterns

### Singleton

Ensures a class has only one instance and provides a global access point to it.

**Use cases:** database connection pool, config manager, logger.

```python
class DatabasePool:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._pool = []  # initialize once
        return cls._instance

pool1 = DatabasePool()
pool2 = DatabasePool()
assert pool1 is pool2  # True
```

**Pitfalls:** global state makes testing hard. Prefer dependency injection when possible.

---

### Factory Method

Defines an interface for creating an object, but lets subclasses decide which class to instantiate. Decouples object creation from usage.

**Use cases:** payment processors, notification senders, storage backends.

```python
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None: ...

class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Email: {message}")

class SMSNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"SMS: {message}")

def get_notifier(channel: str) -> Notifier:
    notifiers = {"email": EmailNotifier, "sms": SMSNotifier}
    cls = notifiers.get(channel)
    if cls is None:
        raise ValueError(f"Unknown channel: {channel}")
    return cls()

notifier = get_notifier("email")
notifier.send("Hello")
```

---

### Builder

Constructs a complex object step by step, separating construction from representation.

**Use cases:** query builders, HTTP request construction, complex config objects.

```python
class QueryBuilder:
    def __init__(self, table: str):
        self._table = table
        self._conditions: list[str] = []
        self._limit: int | None = None

    def where(self, condition: str) -> "QueryBuilder":
        self._conditions.append(condition)
        return self

    def limit(self, n: int) -> "QueryBuilder":
        self._limit = n
        return self

    def build(self) -> str:
        query = f"SELECT * FROM {self._table}"
        if self._conditions:
            query += " WHERE " + " AND ".join(self._conditions)
        if self._limit is not None:
            query += f" LIMIT {self._limit}"
        return query

query = QueryBuilder("users").where("age > 18").where("active = true").limit(10).build()
# SELECT * FROM users WHERE age > 18 AND active = true LIMIT 10
```

---

## Structural Patterns

### Repository

Abstracts the data access layer, decoupling business logic from persistence. The domain code talks to a repository interface; the implementation handles the DB.

**Use cases:** almost every backend service with a database.

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str

class UserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: int) -> User | None: ...

    @abstractmethod
    def save(self, user: User) -> None: ...

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._store: dict[int, User] = {}

    def get_by_id(self, user_id: int) -> User | None:
        return self._store.get(user_id)

    def save(self, user: User) -> None:
        self._store[user.id] = user

# In tests, swap in the in-memory repo; in prod, use a SQL repo.
```

---

### Decorator

Attaches additional responsibilities to an object dynamically. Wraps the original object and adds behavior before/after calling it.

**Use cases:** caching, logging, rate limiting, auth middleware.

```python
from functools import wraps
import time

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.3f}s")
        return result
    return wrapper

# Class-based version for stateful decoration (e.g., caching):
class CachedRepository:
    def __init__(self, repo: UserRepository):
        self._repo = repo
        self._cache: dict[int, User] = {}

    def get_by_id(self, user_id: int) -> User | None:
        if user_id not in self._cache:
            self._cache[user_id] = self._repo.get_by_id(user_id)
        return self._cache[user_id]

    def save(self, user: User) -> None:
        self._cache.pop(user.id, None)  # invalidate
        self._repo.save(user)
```

---

### Proxy

A surrogate that controls access to another object. Unlike Decorator, its purpose is access control, lazy initialization, or remote access — not adding behavior.

**Use cases:** lazy loading, access control, circuit breaker wrapper.

```python
class SecureUserRepository(UserRepository):
    def __init__(self, repo: UserRepository, current_user_role: str):
        self._repo = repo
        self._role = current_user_role

    def get_by_id(self, user_id: int) -> User | None:
        if self._role not in ("admin", "support"):
            raise PermissionError("Access denied")
        return self._repo.get_by_id(user_id)

    def save(self, user: User) -> None:
        if self._role != "admin":
            raise PermissionError("Only admins can write")
        self._repo.save(user)
```

---

### Facade

Provides a simplified interface to a complex subsystem. Hides the complexity of multiple components behind a single entry point.

**Use cases:** service orchestration, SDK wrappers, aggregating microservice calls.

```python
class OrderService:
    """Facade over inventory, payment, and notification subsystems."""

    def __init__(self, inventory, payment, notifier):
        self._inventory = inventory
        self._payment = payment
        self._notifier = notifier

    def place_order(self, user_id: int, item_id: int, amount: float) -> None:
        self._inventory.reserve(item_id)
        self._payment.charge(user_id, amount)
        self._notifier.send(f"Order confirmed for user {user_id}")
```

---

## Behavioral Patterns

### Strategy

Defines a family of algorithms, encapsulates each one, and makes them interchangeable at runtime.

**Use cases:** sorting strategies, pricing rules, authentication methods, compression algorithms.

```python
from abc import ABC, abstractmethod

class PricingStrategy(ABC):
    @abstractmethod
    def calculate(self, base_price: float) -> float: ...

class RegularPricing(PricingStrategy):
    def calculate(self, base_price: float) -> float:
        return base_price

class MemberPricing(PricingStrategy):
    def calculate(self, base_price: float) -> float:
        return base_price * 0.9  # 10% discount

class PriceCalculator:
    def __init__(self, strategy: PricingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PricingStrategy) -> None:
        self._strategy = strategy

    def get_price(self, base_price: float) -> float:
        return self._strategy.calculate(base_price)
```

---

### Observer

Defines a one-to-many dependency. When one object (subject) changes state, all its dependents (observers) are notified automatically.

**Use cases:** event systems, domain events, pub/sub, webhooks, audit logs.

```python
from abc import ABC, abstractmethod

class Event:
    def __init__(self, name: str, data: dict):
        self.name = name
        self.data = data

class EventHandler(ABC):
    @abstractmethod
    def handle(self, event: Event) -> None: ...

class EventBus:
    def __init__(self):
        self._handlers: dict[str, list[EventHandler]] = {}

    def subscribe(self, event_name: str, handler: EventHandler) -> None:
        self._handlers.setdefault(event_name, []).append(handler)

    def publish(self, event: Event) -> None:
        for handler in self._handlers.get(event.name, []):
            handler.handle(event)

# Usage:
class AuditLogger(EventHandler):
    def handle(self, event: Event) -> None:
        print(f"AUDIT: {event.name} — {event.data}")

bus = EventBus()
bus.subscribe("user.created", AuditLogger())
bus.publish(Event("user.created", {"user_id": 42}))
```

---

### Command

Encapsulates a request as an object, allowing you to parameterize actions, queue them, log them, and support undo.

**Use cases:** task queues, undo/redo, audit trails, request batching.

```python
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...

    @abstractmethod
    def undo(self) -> None: ...

class CreateUserCommand(Command):
    def __init__(self, repo: UserRepository, user: User):
        self._repo = repo
        self._user = user

    def execute(self) -> None:
        self._repo.save(self._user)

    def undo(self) -> None:
        pass  # delete the user

class CommandQueue:
    def __init__(self):
        self._history: list[Command] = []

    def execute(self, cmd: Command) -> None:
        cmd.execute()
        self._history.append(cmd)

    def undo_last(self) -> None:
        if self._history:
            self._history.pop().undo()
```

---

### Unit of Work

Tracks all changes made during a business transaction and commits (or rolls back) them as a single atomic operation.

**Use cases:** database transactions, ensuring consistency across multiple repository writes.

```python
class UnitOfWork:
    def __init__(self, session):
        self._session = session
        self.users = UserRepository(session)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, *_):
        if exc_type:
            self._session.rollback()
        else:
            self._session.commit()

# Usage:
with UnitOfWork(db_session) as uow:
    user = User(id=1, name="Alice", email="alice@example.com")
    uow.users.save(user)
    # Commits on success, rolls back on exception.
```

---

## Dependency Injection

Not a GoF pattern, but essential for testable backend code. Instead of a class constructing its dependencies, they are passed in from outside (constructor injection is most common).

```python
# Bad: hard-coded dependency
class OrderService:
    def __init__(self):
        self._db = PostgresDatabase()  # coupled to Postgres

# Good: inject the dependency
class OrderService:
    def __init__(self, db: DatabaseConnection):
        self._db = db  # test with an in-memory DB, prod with Postgres
```

**Why it matters:** enables unit testing without real databases/services, makes dependencies explicit, and supports swapping implementations (e.g., swapping email for SMS).

---

## Summary Table

| Pattern | Category | Key Idea |
|---|---|---|
| Singleton | Creational | One shared instance |
| Factory Method | Creational | Delegate instantiation to a function/subclass |
| Builder | Creational | Step-by-step construction via chained calls |
| Repository | Structural | Abstract data access behind an interface |
| Decorator | Structural | Wrap object to add behavior (caching, logging) |
| Proxy | Structural | Control access (auth, lazy-load, circuit breaker) |
| Facade | Structural | Single entry point to a complex subsystem |
| Strategy | Behavioral | Swap algorithms at runtime |
| Observer | Behavioral | Notify subscribers on state change (events) |
| Command | Behavioral | Encapsulate requests as objects (queues, undo) |
| Unit of Work | Behavioral | Atomic commit across multiple repositories |
| Dependency Injection | — | Pass dependencies in; don't construct them |
