import pytest
from leetcode.problem_solving.two_sum import (
    Solution,
)  # Replace 'your_module' with your actual file/module name


class TestTwoSum:
    solution = Solution()

    @pytest.mark.parametrize(
        "nums, target, expected",
        [
            # Example 1
            ([2, 7, 11, 15], 9, [0, 1]),
            # Example 2
            ([3, 2, 4], 6, [1, 2]),
            # Example 3
            ([3, 3], 6, [0, 1]),
            # Edge case: negative numbers
            ([-3, 4, 3, 90], 0, [0, 2]),
            # Edge case: answer at the end
            ([1, 2, 3, 4, 6], 10, [3, 4]),
            # Edge case: minimal input size
            ([1, 2], 3, [0, 1]),
        ],
    )
    def test_two_sum(self, nums, target, expected):
        result = self.solution.two_sum(nums, target)
        assert sorted(result) == sorted(expected)
