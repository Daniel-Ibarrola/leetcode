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
