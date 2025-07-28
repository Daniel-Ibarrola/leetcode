import pytest
from leetcode.matrix.set_matrix_zeros import Solution


class TestSetMatrixZeroes:
    solution = Solution()

    @pytest.mark.parametrize(
        "matrix, expected",
        [
            # Example 1
            ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
            # Example 2
            (
                [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
                [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
            ),
            # Single row with zero
            ([[1, 2, 0, 4]], [[0, 0, 0, 0]]),
            # Single column with zero
            ([[1], [0], [3]], [[0], [0], [0]]),
            # No zeros
            ([[1, 2], [3, 4]], [[1, 2], [3, 4]]),
            # All zeros
            ([[0, 0], [0, 0]], [[0, 0], [0, 0]]),
            # Edge case: 1x1 with 0
            ([[0]], [[0]]),
            # Edge case: 1x1 with non-zero
            ([[7]], [[7]]),
        ],
    )
    def test_set_zeroes(self, matrix, expected):
        self.solution.set_zeroes(matrix)
        assert matrix == expected
