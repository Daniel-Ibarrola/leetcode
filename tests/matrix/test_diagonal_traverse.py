# test_diagonal_traverse.py

import pytest
from leetcode.matrix.diagonal_traverse import (
    Solution,
)  # make sure your function is in solution.py


class TestDiagonalTraverse:
    solution = Solution()

    @pytest.mark.parametrize(
        "mat, expected",
        [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 4, 7, 5, 3, 6, 8, 9]),
            ([[1, 2], [3, 4]], [1, 2, 3, 4]),
            ([[1, 2, 3, 4]], [1, 2, 3, 4]),  # Single row
            ([[1], [2], [3], [4]], [1, 2, 3, 4]),  # Single column
            ([[42]], [42]),  # Single element
            ([[1, 2, 3, 4], [5, 6, 7, 8]], [1, 2, 5, 6, 3, 4, 7, 8]),  # More columns
            ([[1, 2], [3, 4], [5, 6]], [1, 2, 3, 5, 4, 6]),  # More rows
        ],
    )
    def test_diagonal_traverse(self, mat: list[list[int]], expected: list[int]):
        assert self.solution.diagonal_traverse(mat) == expected
