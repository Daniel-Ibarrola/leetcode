import pytest
from leetcode.transformations.rotate_array import Solution


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),  # Example 1
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),  # Example 2
        ([1, 2], 0, [1, 2]),  # k = 0 (no rotation)
        ([1, 2], 2, [1, 2]),  # k == len(nums)
        ([1, 2, 3], 4, [3, 1, 2]),  # k > len(nums)
        ([1], 10, [1]),  # single element
        ([1, 2, 3, 4, 5], 1, [5, 1, 2, 3, 4]),  # basic right shift
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),  # full rotation (same array)
        ([1, 2, 3, 4, 5], 100000, [1, 2, 3, 4, 5]),  # very large k % n == 0
        ([1, 2, 3, 4, 5], 100003, [3, 4, 5, 1, 2]),  # very large k with remainder
    ],
)
def test_rotate_array(nums, k, expected):
    Solution.rotate(nums, k)
    assert nums == expected
