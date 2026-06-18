# Python Questions

## What are generators in Python?

A **generator** is a special kind of iterator in Python that allows you to iterate over a sequence of values without creating the entire sequence in memory at once. It's a way to create iterators easily.

Generators are defined like regular functions but use the **`yield`** keyword instead of `return` to produce a value. When a generator function is called, it returns a generator object. The code inside the function doesn't execute until you start iterating over it.

Each time you ask the generator for the next value (e.g., in a `for` loop), its execution resumes from where it last left off (after the `yield`) until it hits the next `yield`. The generator's state (its local variables) is saved between calls.

**Key Benefits:**

*   **Memory Efficiency:** Generators produce values one at a time, so they are incredibly memory-efficient for working with very large or infinite sequences.
*   **Laziness:** They compute values only when requested, which can save CPU time if you don't end up needing all the values.

**Example: A list vs. a generator**

Imagine you need the first one million square numbers.

**Using a list (high memory usage):**

```python
def make_list_of_squares(n):
    result = []  # A huge list is created in memory
    for i in range(n):
        result.append(i * i)
    return result

# This will create a list with 1,000,000 integers, consuming a lot of memory.
squares = make_list_of_squares(1_000_000)
```

**Using a generator (low memory usage):**

```python
def generate_squares(n):
    for i in range(n):
        # 'yield' produces a value and pauses execution.
        yield i * i

# The generator object is created, but no squares are calculated yet.
squares_generator = generate_squares(1_000_000)

# The generator calculates one value at a time as the loop requests it.
# Memory usage is minimal, only storing one value at a time.
for sq in squares_generator:
    # do something with sq
    pass
```


There is also a compact syntax called a **generator expression**, which looks like a list comprehension but with parentheses: `(i * i for i in range(1_000_000))`.

---

## 2. What is a decorator in Python?

A **decorator** is a design pattern in Python that allows you to add new functionality to an existing object (like a function or a class) without modifying its source code.

In essence, a decorator is a **function that takes another function as input, adds some functionality to it, and returns another function**. This is possible because in Python, functions are first-class citizens.

Decorators are syntactic sugar, typically written with the `@decorator_name` syntax on top of the function being decorated.

**Common Use Cases:**

*   Logging or timing function execution.
*   Enforcing access control or authentication.
*   Caching or memoizing return values.
*   Validating input or transforming output.

**Example:**

Let's create a simple decorator that prints a message before and after a function runs.

```python
# This is the decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # This is where the original function runs
        print("Something is happening after the function is called.")
    return wrapper

# Using the decorator with the @ syntax
@my_decorator
def say_hello():
    print("Hello!")

# Now, when we call say_hello(), it's actually calling the 'wrapper' function.
say_hello()
```

This will output:
```
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```


The code with the `@` syntax is just a cleaner way of writing `say_hello = my_decorator(say_hello)`.

---

## What are context managers in Python?

A **context manager** is an object that defines a temporary context for a block of code. It is responsible for setting up a resource before the block of code is entered and cleaning it up afterward, even if errors occur within the block.

The primary use case is to manage resources like file handles, network connections, or database sessions, ensuring they are always properly closed.

Context managers are most commonly used with the **`with`** statement.

**How it works:**
A context manager must implement two special methods:

1.  `__enter__()`: This method is executed at the start of the `with` block. It sets up the resource and can optionally return an object to be used within the block (assigned using the `as` keyword).
2.  `__exit__(exc_type, exc_value, traceback)`: This method is executed when the `with` block is exited, either normally or due to an exception. It handles the cleanup. If an exception occurred, the details are passed as arguments, allowing for specific error handling.

**Example:**

The most common example is `open()`, which acts as a context manager for file operations.

```python
# The 'with' statement ensures the file is automatically closed.
with open('example.txt', 'w') as f:
    f.write('Hello, world!')
    # No need to call f.close(). The context manager handles it.
# Once this block is exited, f is guaranteed to be closed.
```


You can also create your own context managers using a class or the `contextlib` module.

**Creating a context manager with a class:**

```python
class Timer:
    def __init__(self):
        print("Timer started")
    
    def __enter__(self):
        import time
        self.start_time = time.time()
        return self # This object is assigned to 't' in the 'with' block

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed_time = time.time() - self.start_time
        print(f"Block executed in: {elapsed_time:.4f} seconds")
        # Returning False here would re-raise any exception that occurred

# Usage
with Timer() as t:
    # Do some time-consuming work
    sum(i for i in range(10_000_000))
```


This provides a robust and reusable way to handle resource setup and teardown, making code safer and more readable.

Of course. Here are the answers to the next set of Python questions.

## 4. What is the difference between a Python package and a Python module?

The difference is about organization and scale. In simple terms, a **module** is a single file, while a **package** is a folder of modules.

#### Module
A **module** is a single Python file (with a `.py` extension) that contains Python code. It can define functions, classes, and variables. The purpose of a module is to group related code, making it easier to understand and use.

You can use the code from a module in another file by using the `import` statement.

**Example of a module:**
File `my_math.py`:
```python
# This entire file is a module named 'my_math'
PI = 3.14159

def add(a, b):
    return a + b
```

**Usage:**
```python
import my_math

result = my_math.add(5, 3)
print(my_math.PI)
```


#### Package
A **package** is a way of organizing related modules into a directory hierarchy. A directory is treated as a package if it contains a special file named `__init__.py`. This file can be empty, but it's essential as it tells Python that the directory is a package, allowing you to import modules from it.

Packages allow you to structure your project's namespace using dot notation (e.g., `my_package.my_module`).

**Example of a package:**
Consider this directory structure:
```
my_app/
├── __init__.py
├── api/
│   ├── __init__.py
│   └── client.py
└── utils/
    ├── __init__.py
    └── formatting.py
```

Here, `my_app`, `api`, and `utils` are all packages. `client.py` and `formatting.py` are modules inside those packages.

**Usage:**
```python
from my_app.api import client
from my_app.utils.formatting import format_text

response = client.get_data()
formatted = format_text("hello")
```


**Summary:**
| Feature       | Module                                | Package                                           |
| :------------ | :------------------------------------ | :------------------------------------------------ |
| **Structure** | A single `.py` file.                  | A directory containing modules and an `__init__.py` file. |
| **Purpose**   | To group related functions and classes. | To organize related modules in a structured hierarchy. |
| **Importing** | `import my_module`                     | `from my_package import my_module`                  |
| **Analogy**   | A page in a book.                     | A chapter in a book, containing multiple pages.     |

---
## What is a metaclass in Python?

A **metaclass** is the "class of a class."

In Python, everything is an object. A number like `5` is an object of the `int` class. A list is an object of the `list` class. In the same way, a **class** (like `MyClass`) is itself an object, and it is an instance of its **metaclass**.

The default metaclass in Python is `type`. When you define a class, Python uses `type` to create it behind the scenes.

In the same way that a class functions as a template for the creation of objects, a metaclass functions as a template for the creation of classes. Metaclasses are sometimes referred to as class factories.

```python
class MyClass:
    pass

# The class 'MyClass' is an object. Its class is 'type'.
print(type(MyClass))  # Output: <class 'type'>
```


**Why would you use one?**
You create a custom metaclass when you want to intercept the **class creation process** itself and modify it. It allows you to run code automatically when a class is defined, not just when an instance is created. This is advanced metaprogramming, used for tasks like:

*   **Registering classes:** Automatically adding a new class to a registry (e.g., for plugins or serializers).
*   **Validating class attributes:** Enforcing rules on a class definition, like ensuring certain methods are implemented or attributes are named correctly.
*   **Injecting attributes or methods:** Automatically adding new methods or attributes to every class that uses the metaclass.

**Example:**
Let's create a metaclass that forces all its classes to have attributes written in `UPPERCASE_SNAKE_CASE`.

```python
# Define the metaclass
class EnforceUppercase(type):
    def __new__(cls, name, bases, attrs):
        # 'attrs' is a dictionary of the class's attributes and methods
        uppercase_attrs = {}
        for attr_name, attr_value in attrs.items():
            if not attr_name.startswith('__'):
                uppercase_attrs[attr_name.upper()] = attr_value
            else:
                uppercase_attrs[attr_name] = attr_value

        # Create the class using the modified attributes
        return super().__new__(cls, name, bases, uppercase_attrs)

# Use the metaclass
class MyConfig(metaclass=EnforceUppercase):
    setting = "value"
    another_setting = 123

# The attributes are now uppercase, even though we defined them in lowercase.
print(hasattr(MyConfig, 'setting'))         # Output: False
print(hasattr(MyConfig, 'SETTING'))         # Output: True
print(MyConfig.ANOTHER_SETTING)             # Output: 123
```

Metaclasses are a powerful but complex feature. In many cases, a class decorator or a simple base class can achieve similar results in a more straightforward way.

---
## Explain the Global Interpreter Lock (GIL)

The **Global Interpreter Lock (GIL)** is a mutex (a type of lock) used in the standard CPython interpreter that prevents multiple native threads from executing Python bytecode at the same time within a single process.

In simpler terms, even if you have a multi-core processor and are using a multithreaded Python program, the GIL ensures that **only one thread can be executing Python code at any given moment.**

**Why does it exist?**
The GIL's primary purpose is to simplify memory management in CPython. Python uses reference counting for garbage collection. The GIL prevents race conditions where two threads might try to modify the reference count of the same object simultaneously, which could lead to memory leaks or incorrect deallocation. It makes writing C extensions for Python much simpler.

**What is the impact?**
The impact of the GIL depends heavily on the type of task your threads are performing:

*   **For CPU-bound tasks:** (e.g., complex calculations, image processing)
    The GIL is a significant performance bottleneck. Because only one thread can run Python code at a time, multithreading provides **concurrency but not parallelism**. The threads will run interleaved on a single CPU core, not simultaneously on multiple cores. For these tasks, the **`multiprocessing`** module is the correct solution, as it uses separate processes, each with its own GIL.

*   **For I/O-bound tasks:** (e.g., waiting for network requests, reading from a file, querying a database)
    The GIL has a much smaller impact. When a thread is waiting for an I/O operation to complete, it **releases the GIL**. This allows another thread to run. So, for tasks involving a lot of waiting, multithreading is still very effective at improving responsiveness and throughput.

**Summary:**
*   It's a lock in the CPython interpreter.
*   It allows only one thread to execute Python bytecode at a time in a single process.
*   It cripples performance for CPU-bound multithreading.
*   It is not a major issue for I/O-bound multithreading.
*   To achieve true parallelism for CPU-bound tasks, you must use `multiprocessing`.
*   The GIL is an implementation detail of CPython. Other Python interpreters like Jython (Java-based) or IronPython (.NET-based) do not have a GIL.

---

## What is the difference between `==` and `is`?

The fundamental difference is that `==` checks for **equality**, while `is` checks for **identity**.

*   `a == b` (Equality): This operator compares the **values** of two objects to see if they are the same. Python calls the `__eq__()` method on the objects to perform this comparison. You use `==` when you care about whether two variables have the same content.

*   `a is b` (Identity): This operator checks if two variables point to the **exact same object in memory**. It returns `True` only if the memory addresses are identical. You use `is` when you want to know if two names refer to the very same object.

**Example with Lists:**
Lists are a great way to see the difference clearly because two different list objects can have the same content.

```python
list_a = [1, 2, 3]
list_b = [1, 2, 3]  # A different list object with the same values
list_c = list_a      # list_c now refers to the same object as list_a

# Comparing for equality (value)
print(f"list_a == list_b: {list_a == list_b}")  # Output: True, because their contents are the same.
print(f"list_a == list_c: {list_a == list_c}")  # Output: True, for the same reason.

print("-" * 20)

# Comparing for identity (memory location)
print(f"list_a is list_b: {list_a is list_b}")  # Output: False, because they are two separate objects in memory.
print(f"list_a is list_c: {list_a is list_c}")  # Output: True, because they both point to the same object.
```


**A Common "Gotcha": Caching**
For performance, Python pre-allocates and caches small integers (typically -5 to 256) and short strings. This means that variables holding these values often *do* point to the same object in memory, which can make `is` behave like `==` unexpectedly.

```python
a = 256
b = 256
print(a is b)  # Output: True (due to integer caching)

x = 257
y = 257
print(x is y)  # Output: False (on most systems, as 257 is not cached)
```


**Rule of thumb:** You should almost always use `==` for comparing values. The main exception is when you specifically need to check for singleton objects, like `None`, where using `is` is idiomatic and slightly faster: `if my_var is None:`.

---

## What are `*args` and `**kwargs`?

`*args` and `**kwargs` are special syntax used in function definitions to pass a **variable number of arguments** to a function. The names `args` and `kwargs` are a convention; you could use `*var` and `**kw` and it would work the same way.

#### `*args` (Non-Keyword Arguments)
The `*args` syntax allows you to pass a variable number of **positional arguments**. These arguments are collected into a **tuple** inside the function.

It's useful when you don't know in advance how many arguments might be passed to your function.

**Example:**
```python
def summarize(*args):
    print(f"Received {len(args)} arguments.")
    print(f"They are of type: {type(args)}")  # It's a tuple!
    total = 0
    for num in args:
        total += num
    return total

# You can call it with any number of positional arguments
print(summarize(1, 2, 3))         # Output: 9
print(summarize(10, 20))          # Output: 30
print(summarize(5))               # Output: 5
```


#### `**kwargs` (Keyword Arguments)
The `**kwargs` syntax allows you to pass a variable number of **keyword arguments** (arguments with names). These arguments are collected into a **dictionary** inside the function, where the keys are the argument names and the values are the argument values.

**Example:**
```python
def display_info(**kwargs):
    print(f"Received {len(kwargs)} keyword arguments.")
    print(f"They are of type: {type(kwargs)}")  # It's a dictionary!
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

# You can call it with any number of keyword arguments
display_info(name="Alice", age=30)
# Output:
# - name: Alice
# - age: 30

display_info(user="Bob", role="Admin", status="Active")
# Output:
# - user: Bob
# - role: Admin
# - status: Active
```

#### Using Them Together
You can combine them in a function definition along with standard arguments. The required order is:
1.  Standard positional arguments
2.  `*args`
3.  Standard keyword-only arguments
4.  `**kwargs`

```python
def complete_function(a, b, *args, default_option="fast", **kwargs):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"args = {args}")
    print(f"default_option = {default_option}")
    print(f"kwargs = {kwargs}")

complete_function(1, 2, 3, 4, 5, user="Charlie", logged_in=True)
```

Output:
```
a = 1
b = 2
args = (3, 4, 5)
default_option = fast
kwargs = {'user': 'Charlie', 'logged_in': True}
```

## What is the difference between `@classmethod`, `@staticmethod`, and instance methods?

A class can have three types of methods, distinguished by how they receive information about the class or instance.

- **Instance methods** receive the instance as the first argument (`self`). They can access and modify both instance and class state. This is the default.
- **`@classmethod`** receives the class as the first argument (`cls`), not the instance. It can access and modify class-level state. Common use case: alternative constructors.
- **`@staticmethod`** receives neither the instance nor the class. It behaves like a regular function scoped to the class namespace — use it for utility logic that is logically related to the class but needs no class or instance data.

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def display(self):  # instance method
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

    @classmethod
    def from_string(cls, date_string):  # alternative constructor
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)

    @staticmethod
    def is_valid_year(year):  # utility — no class/instance needed
        return 1 <= year <= 9999

d1 = Date(2025, 6, 18)
d2 = Date.from_string("2025-06-18")
print(Date.is_valid_year(2025))  # True
```

---

## What is the difference between `__repr__` and `__str__`?

Both define a string representation of an object, but they serve different audiences:

- `__str__` is **human-readable** — the informal, user-facing string. Called by `str()` and `print()`.
- `__repr__` is **unambiguous** and developer-facing — ideally a string that could recreate the object in Python. Called by `repr()` and in the interactive REPL.

If `__str__` is not defined, Python falls back to `__repr__`. The reverse is not true.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(1, 2)
print(str(p))   # (1, 2)         — calls __str__
print(repr(p))  # Point(x=1, y=2) — calls __repr__
print(p)        # (1, 2)         — print() calls __str__
```

Rule of thumb: always implement `__repr__`. Add `__str__` only when you want a display distinct from the repr.

---

## How does multiple inheritance work, and what is the MRO?

Python supports multiple inheritance, where a class can inherit from more than one base class. The **Method Resolution Order (MRO)** is the order Python searches classes when looking up a method or attribute.

Python uses the **C3 linearization algorithm**, which guarantees:
1. A class always comes before its parents.
2. The original ordering of parent classes is preserved.

You can inspect the MRO with `ClassName.__mro__`.

```python
class A:
    def who(self): return "A"

class B(A):
    def who(self): return "B"

class C(A):
    def who(self): return "C"

class D(B, C):
    pass

print(D().who())   # B
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

`super()` respects the MRO, making cooperative multiple inheritance safe:

```python
class Base:
    def greet(self):
        print("Base")

class Mixin:
    def greet(self):
        print("Mixin")
        super().greet()

class Child(Mixin, Base):
    def greet(self):
        print("Child")
        super().greet()

Child().greet()
# Child
# Mixin
# Base
```

---

## What is the `@property` decorator?

`@property` lets you define a method that is accessed like an attribute — no parentheses. It allows you to add validation or computed logic behind what looks like a plain attribute, without changing the public API.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

c = Circle(5)
print(c.radius)  # 5
print(c.area)    # 78.539...
c.radius = 10    # calls the setter
c.radius = -1    # raises ValueError
```

Key use cases: input validation on assignment, computed/derived attributes, and transitioning from a plain attribute to controlled access without breaking callers.

---

## What is a closure?

A **closure** is a function that remembers variables from its enclosing scope even after that scope has finished executing. The inner function "closes over" those variables.

```python
def make_counter(start=0):
    count = start

    def increment():
        nonlocal count  # required to modify an enclosing variable
        count += 1
        return count

    return increment

counter = make_counter()
print(counter())  # 1
print(counter())  # 2

counter2 = make_counter(10)
print(counter2())  # 11 — independent state
```

Closures are the mechanism behind decorators. A common pitfall is the **late binding** problem in loops — all closures share the same variable reference, not its value at creation time:

```python
# Bug: all functions see the final value of i
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])  # [2, 2, 2]

# Fix: capture the value at definition time via a default argument
funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])  # [0, 1, 2]
```

---

## What are some useful tools in `functools`?

`functools` is a standard library module for higher-order functions. The most interview-relevant tools:

**`lru_cache`** — memoizes function results based on arguments. Essential for recursive algorithms.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(50))          # Instant, results are cached
print(fib.cache_info()) # CacheInfo(hits=48, misses=51, ...)
```

**`wraps`** — preserves the metadata (name, docstring) of the original function when writing decorators. Without it, the wrapped function loses its identity.

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Say hello."""
    print(f"Hello, {name}!")

print(greet.__name__)  # greet (not 'wrapper')
print(greet.__doc__)   # Say hello.
```

**`partial`** — creates a new callable with some arguments pre-filled.

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(4))  # 16
print(cube(3))    # 27
```

---

## What is the difference between `copy` and `deepcopy`?

Both functions from the `copy` module duplicate an object, but differ in how they handle nested objects.

- **`copy.copy()`** — shallow copy: a new object, but with references to the **same** nested objects as the original.
- **`copy.deepcopy()`** — deep copy: a new object with **fully independent** copies of all nested objects.

```python
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0].append(99)

print(original)  # [[1, 2, 99], [3, 4]]
print(shallow)   # [[1, 2, 99], [3, 4]] — affected! shares inner list
print(deep)      # [[1, 2], [3, 4]]     — unaffected, fully independent
```

Use `copy()` when the object has no nested mutable state, or when sharing nested references is intentional. Use `deepcopy()` when you need a fully independent clone.

---

## What does the `collections` module provide?

`collections` offers specialized container types beyond the built-ins. The most commonly used:

**`defaultdict`** — a dict that returns a default value for missing keys instead of raising `KeyError`.

```python
from collections import defaultdict

word_count = defaultdict(int)
for word in ["apple", "banana", "apple", "cherry", "banana", "apple"]:
    word_count[word] += 1

print(dict(word_count))  # {'apple': 3, 'banana': 2, 'cherry': 1}
```

**`Counter`** — counts occurrences of elements in any iterable.

```python
from collections import Counter

counts = Counter(["apple", "banana", "apple", "cherry"])
print(counts.most_common(2))  # [('apple', 2), ('banana', 1)]
```

**`deque`** — a double-ended queue with O(1) appends and pops from both ends. Prefer it over `list` when you frequently add or remove from the left.

```python
from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)  # O(1)
dq.popleft()      # O(1)
print(dq)         # deque([1, 2, 3])
```

**`namedtuple`** — a tuple subclass with named fields, useful for lightweight, immutable records.

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(x=1, y=2)
print(p.x, p.y)   # 1 2
print(p[0])       # 1 — still indexable like a tuple
```

---

## What are type hints in Python?

Type hints (PEP 484, Python 3.5+) are optional annotations indicating the expected types of variables, parameters, and return values. They do **not** enforce types at runtime — Python remains dynamically typed — but they enable static analysis tools (`mypy`, `pyright`) to catch type errors before running code, and improve IDE autocomplete and readability.

```python
from typing import Optional

def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()

def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)  # returns str or None
```

For collections, use the built-in generic syntax (Python 3.9+):

```python
def process(items: list[int]) -> dict[str, int]:
    return {"total": sum(items), "count": len(items)}
```

`typing` also provides `Union`, `Any`, `Callable`, `TypeVar`, `Protocol`, and `Literal` for more complex cases.

---

## What is the difference between `dataclass` and `namedtuple`?

Both bundle data fields into a class, but they differ in mutability and flexibility:

| Feature | `dataclass` | `namedtuple` |
|:---|:---|:---|
| **Mutability** | Mutable by default (can be frozen) | Always immutable |
| **Memory** | Slightly more overhead | More efficient (tuple-backed) |
| **Inheritance** | Full class inheritance | Limited |
| **Custom methods** | Yes | Limited |
| **Mutable defaults** | Via `field(default_factory=...)` | Not supported |

```python
from dataclasses import dataclass, field

@dataclass
class Inventory:
    name: str
    quantity: int = 0
    tags: list[str] = field(default_factory=list)

    def restock(self, amount: int):
        self.quantity += amount

item = Inventory("Widget", 10)
item.restock(5)
print(item)  # Inventory(name='Widget', quantity=15, tags=[])
```

Use `namedtuple` for lightweight, immutable records where tuple-like behavior (indexing, unpacking) is useful. Use `dataclass` when you need mutability, methods, or complex defaults.

---

## How does exception handling work in Python?

Python uses a `try / except / else / finally` structure:
- `except` — catches specific exceptions.
- `else` — runs only if no exception was raised.
- `finally` — always runs; use it for cleanup.

```python
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError as e:
        print(f"Invalid types: {e}")
        return None
    else:
        print("Division successful")
        return result
    finally:
        print("Always runs")
```

**Custom exceptions** — inherit from `Exception` to create domain-specific errors:

```python
class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f"Cannot withdraw {amount}, balance is {balance}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
    return balance - amount
```

Avoid bare `except:` — it also catches `SystemExit` and `KeyboardInterrupt`. Catch `Exception` or a specific subclass instead.

---

## What does `if __name__ == '__main__'` mean?

Every Python module has a `__name__` attribute. When a file is **run directly** (`python my_script.py`), `__name__` is set to `'__main__'`. When it is **imported**, `__name__` is set to the module's name.

This idiom lets you write code that only runs when the file is executed directly — not when imported as a library.

```python
def compute(x):
    return x * 2

def main():
    print(compute(5))

if __name__ == '__main__':
    main()
```

Without this guard, `main()` would run every time any other file imports `compute`, which is almost never desired.

---

## What is the walrus operator (`:=`)?

The walrus operator (`:=`), introduced in Python 3.8 (PEP 572), is the **assignment expression** operator. It assigns a value to a variable and returns that value within an expression, allowing you to avoid computing or calling something twice.

```python
data = [1, 2, 3, 4, 5]

# Without walrus: len() called twice
if len(data) > 3:
    print(f"Long list: {len(data)} items")

# With walrus: computed once, used in both the check and the body
if (n := len(data)) > 3:
    print(f"Long list: {n} items")
```

Commonly used in `while` loops to read and check a value in one step:

```python
import re

text = "Error on line 42: file not found"
if match := re.search(r'line (\d+)', text):
    print(f"Found error at line {match.group(1)}")  # Found error at line 42
```

---

## What is the difference between mutable and immutable objects?

In Python, every object is either **mutable** or **immutable**. This refers to whether the object's state or content can be changed after it is created.

#### Immutable Objects
An **immutable** object cannot be modified after it is created. If you try to change the value of an immutable object, Python actually creates a *new* object in memory with the new value.

**Common Immutable Types:**
*   **Numbers:** `int`, `float`, `complex`
*   **Strings:** `str`
*   **Tuples:** `tuple`
*   **Frozen Sets:** `frozenset`
*   **Booleans:** `bool`

**Example:**
```python
s = "Hello"
# Attempting to change a character will raise a TypeError
# s[0] = "h"  

# This creates a NEW string object; the original "Hello" remains unchanged until garbage collected.
s = s + " World" 
```

#### Mutable Objects
A **mutable** object can be changed after it is created without changing its identity (memory address). You can add, remove, or modify its contents in place.

**Common Mutable Types:**
*   **Lists:** `list`
*   **Dictionaries:** `dict`
*   **Sets:** `set`
*   **Byte Arrays:** `bytearray`

**Example:**
```python
my_list = [1, 2, 3]
my_list.append(4)  # Modifies the same object in memory
my_list[0] = 99    # Changes an element in place
print(my_list)     # Output: [99, 2, 3, 4]
```

#### Why it matters?
Understanding mutability is crucial because:
1.  **Efficiency:** Mutable objects are often more efficient for large collections since they don't require copying the entire structure for every change.
2.  **Function Arguments:** When you pass a mutable object to a function, the function can modify the original object. Immutable objects are safe from such side effects.
3.  **Dictionary Keys:** Only immutable objects can be used as keys in a dictionary (or elements in a set) because their hash value must remain constant.

