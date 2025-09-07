# General Programming Questions

## Explain concurrency in a high level. Async, multithreading, multiprocessing, etc.

At a high level, **concurrency** is the concept of a program structuring its work into tasks that can be managed and run in overlapping time periods. It's about _dealing_ with many things at once.
This is often confused with **parallelism**, which is about _doing_ many things at once. Parallelism requires hardware with multiple cores or processors. Concurrency is a way to structure your code to _enable_ parallelism if the hardware is available, but it's also useful on a single core to improve responsiveness and handle waiting for external resources efficiently.
Here’s a breakdown of the common models for achieving concurrency:

### Multiprocessing
- **What it is:** This model uses multiple independent processes, where each process has its own memory space and runs on a separate CPU core.
- **Analogy:** Imagine a restaurant with several separate, fully-equipped kitchens. Each kitchen is a **process**. They can all cook full meals in parallel. If one kitchen needs something from another, they have to use a specific communication channel (like a dumbwaiter), which is a deliberate and relatively slow action.
- **When to use it:** It's best for **CPU-bound tasks**—computationally heavy work that can be broken down into independent chunks (e.g., video processing, large-scale data analysis). Because the processes don't share memory, it's a way to bypass Python's Global Interpreter Lock (GIL) and achieve true parallelism.
- **Pros:**
    - Achieves true parallelism, utilizing multiple CPU cores.
    - Memory isolation means one process crashing won't affect others.

- **Cons:**
    - Higher memory usage since memory isn't shared.
    - Inter-Process Communication (IPC) is slower and more complex than communication between threads.

### Multithreading
- **What it is:** This model uses multiple threads of execution within a single process. All threads share the same memory space.
- **Analogy:** Imagine a single large kitchen (the **process**) with several chefs (the **threads**). They all share the same ingredients and equipment (the **memory**). They can work on different tasks, but they must be careful not to get in each other's way (e.g., two chefs trying to use the same knife).
- **When to use it:** It's best for **I/O-bound tasks**. These are tasks where the program spends most of its time waiting for something external, like a network request to finish or a file to be read from a disk. While one thread is waiting, the system can switch to another thread to do useful work.
- **Pros:**
    - Lower memory footprint than multiprocessing.
    - Sharing data between threads is easy because they share memory.

- **Cons:**
    - In CPython, the Global Interpreter Lock (GIL) prevents multiple threads from executing Python code at the same time, so it doesn't help with CPU-bound tasks.
    - Shared memory can lead to race conditions and deadlocks, requiring complex synchronization tools like locks to manage safely.

### Asynchronous Programming (Async/Await)
- **What it is:** This is a concurrent programming paradigm that runs on a **single thread**. An event loop manages multiple tasks. When a task reaches a point where it has to wait for I/O, it explicitly tells the event loop, "I'm waiting," and yields control. The event loop then runs another task that is ready to do work.
- **Analogy:** Imagine a single, highly-efficient chef in a kitchen. The chef starts cooking a steak (Task A). When the steak needs to sear for five minutes (an I/O wait), the chef doesn't just stand there. They set a timer and immediately start chopping vegetables for a salad (Task B). When the timer rings (the event loop signals completion), the chef can switch back to the steak. The key is that the chef is never idle and only works on one thing at a exact moment.
- **When to use it:** It excels at **high-volume I/O-bound tasks**, like a web server handling thousands of simultaneous network connections. It is far more efficient in terms of memory and context-switching overhead than multithreading for these scenarios.
- **Pros:**
    - Extremely efficient with very low overhead, allowing for tens of thousands of concurrent operations.
    - No risk of race conditions in the same way as multithreading, as control is explicitly yielded, not preemptively taken away.

- **Cons:**
    - Doesn't help at all with CPU-bound tasks; a long-running computation will block the entire event loop.
    - Requires a different style of programming and for your code (and the libraries you use) to be designed to support the `async/await` model.

### Summary: Which One to Choose?
- **For CPU-bound tasks:** Use **multiprocessing** to leverage multiple cores.
- **For I/O-bound tasks:** **Multithreading** is a solid, traditional choice.
- **For a massive number of I/O-bound tasks:** **Async** is the most scalable and efficient solution.

## What are fixtures?

In software testing, a **fixture** is a way to provide a consistent, baseline environment for your tests. It handles the setup and teardown of resources, ensuring that every test starts from a known state.
Think of it as the "Arrange" step in the **Arrange-Act-Assert** testing pattern.

Example in `pytest`
`pytest` has a powerful fixture system that makes this concept very clear.

```python
def test_adding_item_to_cart():
    cart = ShoppingCart()  # Repetitive setup
    cart.add_item("apple")
    assert cart.get_total_items() == 1

def test_initial_cart_is_empty():
    cart = ShoppingCart()  # Repetitive setup
    assert cart.get_total_items() == 0
```
**Without a fixture (repetitive setup)**
```python
import pytest

@pytest.fixture
def cart():
    """Provides a new ShoppingCart instance for each test."""
    return ShoppingCart()

def test_adding_item_to_cart(cart):  # Fixture is injected as an argument
    cart.add_item("apple")
    assert cart.get_total_items() == 1

def test_initial_cart_is_empty(cart):
    assert cart.get_total_items() == 0
```

## SOLID Principles

SOLID is an acronym for five design principles for object-oriented programming that are intended to make software designs more understandable, flexible, and maintainable. They were promoted by Robert C. Martin.
Here's a breakdown of each principle:

### S - Single Responsibility Principle (SRP)
- **The Idea:** A class should have only one reason to change.
- **In other words:** A class should have only one job or responsibility. If a class does more than one thing, it is more likely to change and more likely that those changes will have unintended side effects.
- **Analogy:** A Swiss Army knife is a violation of this principle. It's a knife, a screwdriver, and a can opener all in one. If you want to change the design of the screwdriver, you are meddling with a tool that also contains a knife. It's better to have a dedicated screwdriver for the screwdriver job.

#### Example

**Bad: Violates SRP** The `Report` class has two responsibilities: compiling the report data and saving it. A change in the save mechanism (e.g., saving to the cloud instead of a file) would require changing the `Report` class.
```python
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def format_report(self):
        return f"<h1>{self.title}</h1><p>{self.content}</p>"

    def save_to_file(self, filename):
        # This is a second responsibility
        with open(filename, 'w') as f:
            f.write(self.format_report())
```
**Good: Follows SRP** Responsibilities are separated into two classes. The `Report` class only handles the data and formatting, while the `PersistenceManager` handles the saving.
```python
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def format_report(self):
        return f"<h1>{self.title}</h1><p>{self.content}</p>"

class PersistenceManager:
    @staticmethod
    def save_to_file(filename, data):
        with open(filename, 'w') as f:
            f.write(data)

# Usage:
report = Report("Monthly Report", "...")
formatted_report = report.format_report()
PersistenceManager.save_to_file("report.html", formatted_report)
```

### O - Open/Closed Principle (OCP)
- **The Idea:** Software entities (classes, modules, functions) should be open for extension but closed for modification.
- **In other words:** You should be able to add new functionality to a class without changing its existing source code.
- **Analogy:** A smartphone. You can extend its functionality by installing new apps (open for extension) without having to modify its internal hardware or core operating system (closed for modification).
- **Example:** Instead of adding an `if-elif-else` block to a function every time you need to handle a new shape, you can use a `Shape` interface with an `area()` method. New shapes (`Circle`, `Rectangle`) can be added by creating new classes that implement this interface, without ever touching the original code that uses the `Shape` interface.

**Bad: Violates OCP** To add a new shape (e.g., a triangle), you must modify the `AreaCalculator` class by adding another `elif` block.
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Circle:
    def __init__(self, radius):
        self.radius = radius

class AreaCalculator:
    def calculate_total_area(self, shapes):
        total_area = 0
        for shape in shapes:
            if isinstance(shape, Rectangle):
                total_area += shape.width * shape.height
            elif isinstance(shape, Circle):
                total_area += 3.14 * shape.radius ** 2
        return total_area
```
**Good: Follows OCP** We use an abstract base class (`Shape`) and polymorphism. To add a new shape, we just create a new class that inherits from `Shape`. The `AreaCalculator` never needs to be changed.
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# To extend, just add a new class:
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

class AreaCalculator:
    def calculate_total_area(self, shapes):
        return sum(shape.area() for shape in shapes)
```


#### L - Liskov Substitution Principle (LSP)
- **The Idea:** Subtypes must be substitutable for their base types.
- **In other words:** If you have a class `B` that is a subclass of `A`, you should be able to use `B` anywhere you would use `A` without the program breaking or behaving unexpectedly. Subclasses should extend the capabilities of the parent class, not narrow them.
- **Analogy:** A remote control for a "TV" (base class) should work just fine for a "Smart TV" (subclass). If pressing the "On" button on the remote causes the Smart TV to do something other than turn on (like order a pizza), it violates this principle.
- **Example:** A classic example is the Rectangle/Square problem. If `Square` inherits from `Rectangle`, and code that uses a `Rectangle` sets its width and height independently, this will break the logic for a `Square` (where width and height must be equal). This suggests `Square` shouldn't be a subtype of `Rectangle` in this model.

**Bad: Violates LSP** A `Square` is not a proper substitute for a `Rectangle`. The `test_area` function, which works for a `Rectangle`, produces an unexpected result when a `Square` is passed to it because the `set_height` method changes `width`.
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

    def set_width(self, width):
        self.width = self.height = width

    def set_height(self, height):
        self.width = self.height = height

def test_area(rect: Rectangle):
    rect.set_width(5)
    rect.set_height(4)
    # Expected area is 20 (5*4), but for Square it's 16 (4*4)
    assert rect.get_area() == 20

# This would fail:
# s = Square(1)
# test_area(s)
```
**Good: Follows LSP** Model the classes based on their behavior. A `Square`'s behavior is different from a `Rectangle`'s, so they shouldn't be in a parent-child relationship in this way. They can both inherit from a more abstract `Shape` if needed.
```python
class Shape(ABC): # From OCP example
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, size):
        self.size = size

    def area(self):
        return self.size ** 2
```

#### I - Interface Segregation Principle (ISP)
- **The Idea:** No client should be forced to depend on methods it does not use.
- **In other words:** It’s better to have many small, specific interfaces than one large, general-purpose one.
- **Analogy:** You don't need a single, giant menu that lists every food item in a city. You just want the menu for the specific restaurant you are in. A class that implements a "fat" interface is like a chef being forced to know how to cook every dish from that giant menu, even if their restaurant only serves Italian food.
- **Example:** Imagine an interface `IWorker` with methods `work()` and `eat()`. A `HumanWorker` class can implement both. But a `RobotWorker` class would be forced to implement `eat()`, which it doesn't do. A better design would be to have separate `IWorkable` and `IEatable` interfaces.

**Bad: Violates ISP** The `OldFashionedPrinter` cannot `scan` or `fax`, but it's forced to implement these methods from the "fat" `IMachine` interface
```python
class IMachine(ABC):
    @abstractmethod
    def print(self, document): pass

    @abstractmethod
    def scan(self, document): pass

    @abstractmethod
    def fax(self, document): pass

class OldFashionedPrinter(IMachine):
    def print(self, document):
        print(f"Printing {document}")

    def scan(self, document):
        raise NotImplementedError("This machine cannot scan")

    def fax(self, document):
        raise NotImplementedError("This machine cannot fax")
```
**Good: Follows ISP** Interfaces are broken down into smaller, role-specific ones. Classes can implement only the interfaces they need.
```python
class IPrinter(ABC):
    @abstractmethod
    def print(self, document): pass

class IScanner(ABC):
    @abstractmethod
    def scan(self, document): pass

class OldFashionedPrinter(IPrinter):
    def print(self, document):
        print(f"Printing {document}")

class Photocopier(IPrinter, IScanner):
    def print(self, document):
        print(f"Printing {document}")
    
    def scan(self, document):
        print(f"Scanning {document}")
```

#### D - Dependency Inversion Principle (DIP)
- **The Idea:**
    1. High-level modules should not depend on low-level modules. Both should depend on abstractions (e.g., interfaces).
    2. Abstractions should not depend on details. Details should depend on abstractions.

- **In other words:** Your code should depend on abstractions (like interfaces or abstract classes), not on concrete implementations. This decouples your code.
- **Analogy:** A lamp doesn't have its power cord permanently wired into the wall's internal circuitry (a low-level detail). Instead, it has a plug (an abstraction) that fits into a standard wall outlet (another abstraction). This allows you to use the lamp with any outlet and vice-versa.
- **Example:** A `ReportGenerator` class (high-level) should not directly create an instance of a `MySQLDatabase` class (low-level). Instead, it should depend on a `Database` interface. This allows you to "inject" any database class (like `MySQLDatabase` or `PostgresDatabase`) that implements the `Database` interface, making the `ReportGenerator` flexible and easier to test. This is the core idea behind **Dependency Injection**.

```python
class MySQLDatabase:
    def connect(self):
        print("Connecting to MySQL...")
    
    def query(self, sql):
        print(f"Querying MySQL: {sql}")
        return "some_data"

class PasswordReminder:
    def __init__(self):
        # Direct dependency on a low-level, concrete class
        self.db_connection = MySQLDatabase()

    def get_users_to_remind(self):
        self.db_connection.connect()
        return self.db_connection.query("SELECT * FROM users WHERE...")
```

## Explain REST APIs. What are the main HTTP verbs?

**REST** stands for **RE**presentational **S**tate **T**ransfer. It is not a protocol or a standard, but an **architectural style** for designing networked applications. A web service or API that follows the principles of REST is called a **RESTful** API.

The core idea of REST is to build APIs on top of the existing, proven technology of the web: the HTTP protocol. Instead of inventing a new set of rules for how a client and server should communicate, REST leverages the standard methods and concepts of HTTP.

---

### Key Principles of REST

To be considered RESTful, an architecture must adhere to several constraints:

1.  **Client-Server Architecture:** The client (e.g., a web browser or mobile app) is responsible for the user interface, while the server is responsible for storing and retrieving data. They are separate concerns and evolve independently.

2.  **Statelessness:** This is a crucial constraint. Every request from a client to a server must contain all the information the server needs to understand and fulfill that request. The server does not store any information about the client's state between requests. If a client state is needed (like being logged in), the client is responsible for sending it with every request (e.g., as an authentication token).

3.  **Cacheability:** Responses from the server should be defined as cacheable or not. This allows clients and intermediaries (like Content Delivery Networks) to store a copy of the response, improving performance and scalability.

4.  **Uniform Interface:** This is the fundamental design principle of REST and simplifies the architecture. It has four sub-constraints:
    *   **Resource-Based:** Everything is a "resource." A resource can be a user, a product, an order—any object of data. Resources are identified by a unique URI (Uniform Resource Identifier), like `/users/123`.
    *   **Manipulation of Resources Through Representations:** The client doesn't get the resource itself; it gets a *representation* of the resource (e.g., a JSON or XML object). The client uses this representation to modify the resource's state on the server.
    *   **Self-Descriptive Messages:** Each request is self-contained. For example, a request specifies that it wants a `application/json` representation, and the response uses a status code like `200 OK` or `404 Not Found` to communicate the outcome.
    *   **HATEOAS (Hypermedia as the Engine of Application State):** A RESTful client should be able to navigate the entire API just by following links provided in the responses from the server. For example, a response for a user might contain a link to view that user's orders.

---

### Main HTTP Verbs (HTTP Methods)

REST uses standard HTTP verbs to perform actions on resources. The most common ones are:

| Verb    | Action                             | Description                                                                                                                              | Idempotent? |
| :------ | :--------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| **GET**     | **Read** a resource                | Retrieves a representation of a resource. This is a safe operation, meaning it doesn't change the resource's state.                      | Yes         |
| **POST**    | **Create** a new resource          | Submits data to be processed to create a new resource. Typically used when the client doesn't know the URI of the new resource beforehand. | No          |
| **PUT**     | **Update/Replace** a resource      | Replaces an existing resource with a new representation. The entire resource must be sent in the request.                                | Yes         |
| **DELETE**  | **Delete** a resource              | Removes a specific resource.                                                                                                             | Yes         |
| **PATCH**   | **Partially Update** a resource    | Applies a partial modification to a resource. Unlike `PUT`, you only need to send the data for the fields you want to change.              | No          |

**What does Idempotent mean?**
An operation is **idempotent** if making the same request multiple times has the same effect as making it once.
*   `GET /users/123` will always return the same user data (safe and idempotent).
*   `DELETE /users/123` will delete the user the first time, and subsequent calls will result in "Not Found," but the state of the system remains the same (user is deleted). So, it's idempotent.
*   `POST /users` will create a new user *every time* you call it. This is **not** idempotent.

#### Example Usage:

Let's imagine a REST API for managing a collection of `articles`.

*   `GET /articles`: Get a list of all articles.
*   `GET /articles/42`: Get the article with ID 42.
*   `POST /articles`: Create a new article. The request body would contain the new article's data (e.g., title, content).
*   `PUT /articles/42`: Completely replace article 42 with the data in the request body.
*   `PATCH /articles/42`: Update just the title of article 42. The request body might just be `{"title": "A New Title"}`.
*   `DELETE /articles/42`: Delete the article with ID 42.
Of course. This is a fundamental concept in software design, and here is a clear explanation suitable for your guide.

## 5. What is the difference between OOP and functional programming?

**Object-Oriented Programming (OOP)** and **Functional Programming (FP)** are two different **paradigms**, or ways of thinking about and structuring code. The fundamental difference lies in what they prioritize: OOP organizes code around **data (objects)**, while FP organizes code around **actions (functions)**.

Most modern languages are multi-paradigm, meaning they support both styles, but understanding the core distinction is key.

---

### Core Concepts at a Glance

| Core Concept           | Object-Oriented Programming (OOP)                                | Functional Programming (FP)                                       |
| :--------------------- | :--------------------------------------------------------------- | :---------------------------------------------------------------- |
| **Primary Unit**       | **Objects**: Data and the methods that operate on that data are bundled together. | **Functions**: Functions are first-class citizens, treated as data themselves. |
| **State Management**   | State is typically **encapsulated and mutable**, modified by methods. | State is generally **avoided and immutable**. Functions produce new state instead of changing old state. |
| **Data vs. Behavior**  | Data and behavior are **tightly coupled** inside objects.        | Data (e.g., structs, lists) and behavior (functions) are **kept separate**. |
| **Primary Goal**       | To model the real world with objects and manage complexity through encapsulation. | To achieve predictability and avoid side effects through pure functions. |
| **Concurrency**        | Can be difficult to manage due to shared, mutable state, often requiring locks. | Easier to manage because of immutability. No shared state means no race conditions. |
| **Flow Control**       | Tends to be **imperative**: `for` loops, `if`/`else` blocks, method calls. | Tends to be **declarative**: Composing functions, function chaining, recursion. |

---

### Detailed Breakdown

#### 1. State

*   **OOP:** The concept of "state" is central. An object holds its own state in its attributes (e.g., `self.name = "Alice"`). Methods on that object are designed to read or, more importantly, **mutate** (change) that state.
*   **FP:** FP seeks to eliminate or minimize **mutable state**. Instead of changing data in place, a function takes data as input and produces a **new** data structure as output, leaving the original unchanged. This property is called **immutability**. Functions that don't rely on or change any external state are called **pure functions**.

#### 2. Data and Functions

*   **OOP:** A `User` object, for example, bundles data (`name`, `email`) with the functions that operate on it (`change_email()`, `is_active()`). The behavior is tied to the data.
*   **FP:** Data is just data—often held in simple structures like dictionaries or lists. Functions are separate entities that are designed to operate on that data. You'd have a `user` dictionary and a separate `change_email(user, new_email)` function that returns a *new* user dictionary.

---

### Code Example

Let's solve a simple problem in both styles: **"Given a list of numbers, calculate the sum of the squares of the even numbers."**

#### OOP Approach (Imperative and State-driven)

Here, we create an object that holds the numbers and has a method to perform the calculation. The method uses a loop and modifies a `total` variable (its internal state).

```python
class NumberProcessor:
    def __init__(self, numbers):
        # State is stored within the object
        self.numbers = numbers

    def sum_of_squared_evens(self):
        # A mutable variable 'total' is used to track state
        total = 0
        # Imperative loop that tells the computer 'how' to do it
        for num in self.numbers:
            if num % 2 == 0:
                total += num * num
        return total

# Usage
processor = NumberProcessor([1, 2, 3, 4, 5])
result = processor.sum_of_squared_evens()
print(result)  # Output: 20 (which is 2*2 + 4*4)
```


#### Functional Programming Approach (Declarative and Stateless)

Here, we create a pipeline of functions. Each function takes data, transforms it, and passes it to the next. No state is stored or modified; we just declare what we want done.

```python
def sum_of_squared_evens(numbers):
    # Declarative pipeline that says 'what' to do
    
    # 1. Filter out the odd numbers
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    
    # 2. Square the remaining numbers (map to a new list)
    squared_evens = map(lambda x: x * x, even_numbers)
    
    # 3. Sum the results
    return sum(squared_evens)

# A more common, compact way to write this in Python:
def sum_of_squared_evens_compact(numbers):
    return sum(x * x for x in numbers if x % 2 == 0)

# Usage
numbers = [1, 2, 3, 4, 5]
result = sum_of_squared_evens_compact(numbers)
print(result)  # Output: 20
```


### When to Use Which?

*   **Use OOP when:**
    *   You are modeling complex systems with distinct "things" that have their own attributes and behaviors (e.g., a GUI with `Button` and `Window` objects, or a game with `Player` and `Enemy` objects).
    *   You need to manage state over a long period, and encapsulation helps keep it organized.

*   **Use FP when:**
    *   You are performing data processing, transformations, or mathematical calculations (e.g., data analysis, scientific computing).
    *   Concurrency and parallelism are important, as immutability makes it much safer.
    *   You want highly predictable and testable code, as pure functions always produce the same output for the same input.