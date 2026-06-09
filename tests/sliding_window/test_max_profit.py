import pytest
from leetcode.sliding_window.max_profit import max_profit


@pytest.mark.parametrize(
    "prices, expected",
    [
        # Example cases
        ([7, 1, 5, 3, 6, 4], 5),   # buy at 1, sell at 6
        ([7, 6, 4, 3, 1], 0),       # strictly decreasing, no profit possible
        # Single element — cannot buy and sell on different days
        ([5], 0),
        # Two elements, profit possible
        ([1, 2], 1),
        # Two elements, no profit
        ([2, 1], 0),
        # All same prices
        ([3, 3, 3, 3], 0),
        # Best buy is not on day 0
        ([5, 4, 3, 2, 8], 6),       # buy at 2, sell at 8
        # Max profit at the very end
        ([1, 2, 3, 4, 5], 4),       # buy at 1, sell at 5
        # Dip then spike
        ([3, 1, 4, 1, 5, 9, 2, 6], 8),  # buy at 1, sell at 9
        # Large input, monotonically increasing
        (list(range(1, 1001)), 999),
        # Large input, monotonically decreasing
        (list(range(1000, 0, -1)), 0),
    ],
)
def test_max_profit(prices: list[int], expected: int):
    assert max_profit(prices) == expected
