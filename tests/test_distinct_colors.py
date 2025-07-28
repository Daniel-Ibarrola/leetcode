import pytest

from leetcode.distinct_colors import Solution


class TestDistinctColors:
    solution = Solution()

    @pytest.mark.parametrize(
        "limit, queries, expected",
        [
            (
                4,
                [[1, 4], [2, 5], [1, 3], [3, 4]],
                [1, 2, 2, 3],  # Example 1
            ),
            (
                4,
                [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]],
                [1, 2, 2, 3, 4],  # Example 2
            ),
            (
                2,
                [[0, 1], [0, 1], [0, 1]],
                [1, 1, 1],  # Color stays the same
            ),
            (
                3,
                [[1, 1], [1, 2], [1, 3], [2, 4]],
                [1, 1, 1, 2],  # Color of ball 1 changes, only last adds a new one
            ),
            (
                5,
                [[2, 10], [2, 10], [3, 10], [2, 5]],
                [1, 1, 1, 2],  # Last update changes color of ball 2
            ),
            (
                0,
                [[0, 100]],
                [1],  # Single ball
            ),
        ],
    )
    def test_counts_distinct_colors(
        self, limit: int, queries: list[list[int]], expected: list[int]
    ):
        assert self.solution.count_distinct_colors(limit, queries) == expected
