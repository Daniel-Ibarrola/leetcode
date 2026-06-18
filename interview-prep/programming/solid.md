# SOLID Principles

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