# OOP and functional programming

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
