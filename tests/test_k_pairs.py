import pytest

from leetcode.k_diff_pairs import Solution


class TestKDiffPairs:
    solution = Solution()

    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([3, 1, 4, 1, 5], 2, 2),  # Example 1: unique pairs are (1, 3) and (3, 5)
            ([1, 2, 3, 4, 5], 1, 4),  # Example 2: (1,2), (2,3), (3,4), (4,5)
            ([1, 3, 1, 5, 4], 0, 1),  # Example 3: only (1,1) is a valid 0-diff pair
            ([1, 2, 3, 4, 5], 0, 0),  # No duplicates, so no 0-diff pair
            ([1, 1, 1, 2, 2], 1, 1),  # Only (1,2) is valid unique pair
            ([1, 1, 1, 1], 0, 1),  # Only (1,1) is counted once
            ([1, 5, 3, 4, 2], 2, 3),  # (1,3), (3,5), (2,4)
            ([], 1, 0),  # Edge case: empty list
        ],
    )
    def test_counts_k_diff_pairs(self, nums: list[int], k: int, expected: int):
        assert self.solution.find_pairs(nums, k) == expected
