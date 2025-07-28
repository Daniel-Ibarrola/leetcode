import pytest

from leetcode.problem_solving.find_occurrences import Solution


class TestFindOccurrences:
    solution = Solution()

    @pytest.mark.parametrize(
        "nums, queries, x, expected",
        [
            ([1, 3, 1, 7], [1, 3, 2, 4], 1, [0, -1, 2, -1]),  # Example 1
            ([1, 2, 3], [10], 5, [-1]),  # Example 2
            ([5, 5, 5, 5], [1, 2, 3, 4, 5], 5, [0, 1, 2, 3, -1]),  # More than available
            ([1, 2, 1, 2, 1], [1, 2, 3], 1, [0, 2, 4]),  # Exactly 3 matches
            ([9, 8, 7], [1], 6, [-1]),  # x doesn't exist at all
            ([1], [1, 2], 1, [0, -1]),  # Single match
            ([1], [1], 2, [-1]),  # No match at all
        ],
    )
    def test_finds_occurrence_indices(
        self, nums: list[int], queries: list[int], x: int, expected: list[int]
    ):
        assert self.solution.count_occurrences(nums, queries, x) == expected
