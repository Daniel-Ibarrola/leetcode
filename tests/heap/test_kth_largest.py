import pytest
from leetcode.heap.kth_largest import find_kth_largest


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        # Basic examples
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        # Sorted ascending
        ([1, 2, 3, 4, 5, 6], 1, 6),
        ([1, 2, 3, 4, 5, 6], 6, 1),
        # Sorted descending
        ([6, 5, 4, 3, 2, 1], 3, 4),
        # Duplicates
        ([2, 2, 2, 2, 2], 3, 2),
        # Negative numbers
        ([-10, -3, -1, -20], 2, -3),
        ([-1, 0, 1], 2, 0),
        # Large `k`
        ([1, 2, 3, 4, 5], 5, 1),
        # Smallest input
        ([1], 1, 1),
    ],
)
def test_kth_largest(nums: list[int], k: int, expected: int):
    assert find_kth_largest(nums, k) == expected
