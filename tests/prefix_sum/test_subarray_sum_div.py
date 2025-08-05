import pytest
from leetcode.prefix_sum.subarray_sum_div import subarrays_sum_divisible_by_k


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        # Example 1
        ([4, 5, 0, -2, -3, 1], 5, 7),
        # Example 2
        ([5], 9, 0),
        # All elements are 0, k=1 => all subarrays are divisible by 1
        ([0, 0, 0], 1, 6),  # 3 single elements + 2 two-element + 1 full subarray
        # Negative numbers and k=5
        ([-1, 2, 9], 2, 2),  # Subarrays: [2], [2, 9]
        # No subarray divisible by k
        ([1, 2, 3, 4, 5], 11, 0),
        # Multiple subarrays divisible
        ([2, -2, 2, -4], 6, 2),
        # Edge case: array of length 1, divisible
        ([3], 3, 1),
        # Edge case: array of length 1, not divisible
        ([3], 5, 0),
    ],
)
def test_subarrays_div_by_k(nums: list[int], k: int, expected: int):
    assert subarrays_sum_divisible_by_k(nums, k) == expected
