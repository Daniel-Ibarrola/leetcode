import pytest

from leetcode.problem_solving.count_nice_subarrays import Solution


class TestCountNiceSubarrays:
    solution = Solution()

    @pytest.mark.parametrize(
        "nums,k,expected",
        [
            ([1, 1, 2, 1, 1], 3, 2),  # Example 1
            ([2, 4, 6], 1, 0),  # Example 2
            ([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2, 16),  # Example 3
        ],
    )
    def test_counts_nice_subarrays(self, nums: list[int], k: int, expected: int):
        assert self.solution.count_nice_subarrays(nums, k) == expected
