# Object-Oriented Programming

## What are the four pillars of OOP?

### 1. Encapsulation

Bundling data (attributes) and the methods that operate on that data into a single unit (a class), and restricting direct access to internal state. The goal is to hide implementation details and expose only a controlled interface.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private — name-mangled to _BankAccount__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(50)
print(account.get_balance())  # 150
# account.__balance  # AttributeError — not directly accessible
```

### 2. Inheritance

A class (subclass) derives attributes and methods from another class (superclass), enabling code reuse and an "is-a" relationship.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"

print(Dog("Rex").speak())  # Rex says Woof
print(Cat("Whiskers").speak())  # Whiskers says Meow
```

### 3. Polymorphism

The ability of different objects to respond to the same interface or method call in their own way. In Python this is achieved through method overriding and duck typing.

```python
class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

shapes = [Circle(5), Rectangle(4, 6)]

# Same call, different behavior — polymorphism
for shape in shapes:
    print(f"{type(shape).__name__}: {shape.area():.2f}")
```

### 4. Abstraction

Hiding complexity behind a simple interface. Users of a class interact with a well-defined API without needing to know the implementation details. In Python, abstraction is enforced using Abstract Base Classes.

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def charge(self, amount: float) -> bool:
        """Charge the customer. Return True on success."""

class StripeProcessor(PaymentProcessor):
    def charge(self, amount):
        print(f"Charging ${amount} via Stripe")
        return True

# PaymentProcessor()  # TypeError — cannot instantiate abstract class
processor = StripeProcessor()
processor.charge(99.99)
```

---

## Encapsulation in Python: access conventions

Python has no true private members — everything is technically accessible. Instead, it uses naming conventions:

| Convention | Meaning |
|:---|:---|
| `name` | Public — part of the API |
| `_name` | Protected — internal use, don't touch from outside by convention |
| `__name` | Private — name-mangled to `_ClassName__name` to avoid subclass conflicts |

```python
class MyClass:
    def __init__(self):
        self.public = "anyone"
        self._protected = "internal use"
        self.__private = "name-mangled"

obj = MyClass()
print(obj.public)            # anyone
print(obj._protected)        # works, but signals "don't do this"
# print(obj.__private)       # AttributeError
print(obj._MyClass__private) # works — name mangling, not true privacy
```

Name mangling exists to prevent accidental overriding in subclasses, not to enforce security.

---

## Abstract Base Classes (ABCs)

The `abc` module lets you define interfaces that subclasses must implement. Attempting to instantiate an abstract class or a subclass that hasn't implemented all abstract methods raises a `TypeError` at instantiation time — not at call time.

```python
from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def get(self, id: int):
        ...

    @abstractmethod
    def save(self, entity) -> None:
        ...

    def exists(self, id: int) -> bool:  # concrete method — subclasses inherit this
        return self.get(id) is not None


class InMemoryRepository(Repository):
    def __init__(self):
        self._store = {}

    def get(self, id):
        return self._store.get(id)

    def save(self, entity):
        self._store[entity["id"]] = entity


repo = InMemoryRepository()
repo.save({"id": 1, "name": "Alice"})
print(repo.get(1))       # {'id': 1, 'name': 'Alice'}
print(repo.exists(1))    # True — inherited concrete method
print(repo.exists(99))   # False
```

ABCs also work with `isinstance` and `issubclass`, making them useful for type-checking without strict inheritance:

```python
print(isinstance(repo, Repository))   # True
print(issubclass(InMemoryRepository, Repository))  # True
```

---

## Class variables vs. instance variables

- **Instance variables** — unique to each object, defined in `__init__` via `self`.
- **Class variables** — shared across all instances, defined at class level.

```python
class Counter:
    count = 0  # class variable — shared

    def __init__(self, name):
        self.name = name       # instance variable — unique
        Counter.count += 1

a = Counter("a")
b = Counter("b")

print(Counter.count)  # 2
print(a.count)        # 2 — reads class variable
print(a.name)         # a
print(b.name)         # b
```

**The common pitfall — mutable class variables:**

```python
class Bad:
    items = []  # shared across ALL instances

class Good:
    def __init__(self):
        self.items = []  # each instance gets its own list

b1, b2 = Bad(), Bad()
b1.items.append(1)
print(b2.items)  # [1] — unintended sharing!

g1, g2 = Good(), Good()
g1.items.append(1)
print(g2.items)  # [] — independent
```

---

## Method overriding

A subclass redefines a method from its parent to change or extend its behavior. Use `super()` to call the parent's version.

```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        return f"{self.make} {self.model}"

    def start(self):
        return "Starting engine"


class ElectricVehicle(Vehicle):
    def __init__(self, make, model, battery_kwh):
        super().__init__(make, model)   # reuse parent __init__
        self.battery_kwh = battery_kwh

    def start(self):                    # override
        return "Powering up silently"

    def describe(self):                 # extend
        return f"{super().describe()} (EV, {self.battery_kwh} kWh)"


ev = ElectricVehicle("Tesla", "Model 3", 75)
print(ev.describe())  # Tesla Model 3 (EV, 75 kWh)
print(ev.start())     # Powering up silently
```

**Rules:**
- The overriding method must have a compatible signature.
- Call `super().method()` when you want to extend rather than fully replace the parent behavior.
- Violating this breaks the **Liskov Substitution Principle** — a subclass should be usable wherever the parent is expected.

---

## Composition vs. inheritance

Both are ways to reuse code. The rule of thumb: prefer composition.

- **Inheritance** models an "is-a" relationship. Use it when the subclass truly is a specialization of the parent.
- **Composition** models a "has-a" relationship. The class delegates behavior to another object it owns.

**Inheritance example (appropriate):**

```python
class Animal:
    def breathe(self):
        return "breathing"

class Dog(Animal):      # Dog IS-A Animal — inheritance is correct
    def speak(self):
        return "Woof"
```

**Inheritance misuse (fragile base class problem):**

```python
class Stack(list):      # Stack IS-A list? No — now append(), remove(), etc. all leak through
    def push(self, item):
        self.append(item)
    def pop_top(self):
        return self.pop()
```

**Composition fix:**

```python
class Stack:            # Stack HAS-A list — cleaner, no leaky API
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop()

    def peek(self):
        return self._data[-1]

    def __len__(self):
        return len(self._data)
```

**Why prefer composition?**
- Avoids tight coupling to the parent class's implementation.
- Easier to swap the internal component (e.g., replace the list with a deque).
- Avoids the fragile base class problem — changes to the parent don't break the child unexpectedly.
- More flexible — a class can compose multiple behaviors without the complexity of multiple inheritance.

Use inheritance when: the "is-a" relationship is genuine, you need polymorphism (treating subclasses uniformly), and the parent API is stable.
