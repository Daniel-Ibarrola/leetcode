import pytest
from leetcode.basic.running_sum import (
    Solution,
)  # Replace 'your_module' with the actual module name


class TestRunningSum:
    solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected",
        [
            # Example 1
            ([1, 2, 3, 4], [1, 3, 6, 10]),
            # Example 2
            ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
            # Example 3
            ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
            # Edge case: single element
            ([5], [5]),
            # Edge case: negative numbers
            ([1, -1, 2, -2, 3], [1, 0, 2, 0, 3]),
            # Edge case: all zeros
            ([0, 0, 0], [0, 0, 0]),
            # Mixed large numbers
            ([10**6, -(10**6), 1], [10**6, 0, 1]),
        ],
    )
    def test_running_sum(self, nums: list[int], expected: list[int]):
        assert self.solution.running_sum(nums) == expected
