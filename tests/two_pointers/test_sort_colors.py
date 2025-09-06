import pytest
from leetcode.two_pointers.sort_colors import sort_colors


@pytest.mark.parametrize(
    "nums, expected",
    [
        # Example cases
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        # Edge cases
        ([0], [0]),  # single element
        ([1], [1]),
        ([2], [2]),
        ([0, 0, 0], [0, 0, 0]),  # all same
        ([1, 1, 1], [1, 1, 1]),
        ([2, 2, 2], [2, 2, 2]),
        # Already sorted
        ([0, 0, 1, 1, 2, 2], [0, 0, 1, 1, 2, 2]),
        # Reverse sorted
        ([2, 2, 1, 1, 0, 0], [0, 0, 1, 1, 2, 2]),
        # Mixed
        ([1, 0, 2, 1, 0, 2], [0, 0, 1, 1, 2, 2]),
        ([0, 2, 1, 0, 2, 1, 0], [0, 0, 0, 1, 1, 2, 2]),
        # Large input with only two values
        ([0, 2, 0, 2, 0, 2], [0, 0, 0, 2, 2, 2]),
        ([1, 2, 1, 2, 1, 2], [1, 1, 1, 2, 2, 2]),
        # Random order
        ([2, 1, 0, 1, 2, 0, 1], [0, 0, 1, 1, 1, 2, 2]),
    ],
)
def test_sort_colors(nums, expected):
    sort_colors(nums)  # in-place modification
    assert nums == expected
