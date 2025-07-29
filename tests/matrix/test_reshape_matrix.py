import pytest
from leetcode.matrix.reshape_matrix import (
    Solution,
)


class TestMatrixReshape:
    solution = Solution()

    @pytest.mark.parametrize(
        "mat, r, c, expected",
        [
            # Example 1: Valid reshape
            ([[1, 2], [3, 4]], 1, 4, [[1, 2, 3, 4]]),
            # Example 2: Invalid reshape (total size mismatch)
            ([[1, 2], [3, 4]], 2, 4, [[1, 2], [3, 4]]),
            # 1x4 → 2x2
            ([[1, 2, 3, 4]], 2, 2, [[1, 2], [3, 4]]),
            # 3x1 → 1x3
            ([[1], [2], [3]], 1, 3, [[1, 2, 3]]),
            # Already in the desired shape
            ([[1, 2], [3, 4]], 2, 2, [[1, 2], [3, 4]]),
            # Invalid reshape due to element mismatch
            ([[1, 2, 3], [4, 5, 6]], 4, 2, [[1, 2, 3], [4, 5, 6]]),
            # 2x3 → 3x2
            ([[1, 2, 3], [4, 5, 6]], 3, 2, [[1, 2], [3, 4], [5, 6]]),
        ],
    )
    def test_matrix_reshape(
        self, mat: list[list[int]], r: int, c: int, expected: list[list[int]]
    ):
        assert self.solution.matrix_reshape(mat, r, c) == expected
