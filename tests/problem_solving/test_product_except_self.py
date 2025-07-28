import pytest
from leetcode.problem_solving.product_except_self import (
    Solution,
)


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([2, 3], [3, 2]),
        ([5], [1]),  # Technically invalid input (length < 2), but edge test
        ([0, 0], [0, 0]),
        ([0, 1], [1, 0]),
        ([1, 0], [0, 1]),
        ([9, 0, -2], [0, -18, 0]),
        ([10, 20, 30, 40, 50], [1200000, 600000, 400000, 300000, 240000]),
    ],
)
def test_product_except_self(nums: list[int], expected: list[int]):
    assert Solution().product_except_self(nums) == expected
