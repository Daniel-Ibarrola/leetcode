import pytest
from leetcode.problem_solving.subarray_sum import (
    Solution,
)  # Replace with your actual module


class TestSubarraySumEqualsK:
    solution = Solution()

    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            # Example 1
            ([1, 1, 1], 2, 2),
            # Example 2
            ([1, 2, 3], 3, 2),
            # All zeroes and k = 0 (every subarray of size >= 1 counts)
            ([0, 0, 0], 0, 6),
            # Negative numbers
            ([1, -1, 0], 0, 3),
            # Larger case
            ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4),
            # Single element equals k
            ([5], 5, 1),
            # No subarrays equal k
            ([1, 2, 3], 10, 0),
            # Subarrays must be contiguous
            ([1, 2, 1, 2, 1], 3, 4),
            # Long positive run
            (list(range(1, 101)), 5050, 1),  # sum of 1 to 100
        ],
    )
    def test_subarray_sum(self, nums, k, expected):
        assert self.solution.subarray_sum(nums, k) == expected
