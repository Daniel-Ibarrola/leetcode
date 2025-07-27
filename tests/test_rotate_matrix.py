import pytest

from leetcode.rotate_matrix import Solution


class TestRotateMatrix:
    solution = Solution()

    @pytest.mark.parametrize(
        "matrix,expected",
        [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
            (
                [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
                [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
            ),
        ],
    )
    def test_rotate_matrix(self, matrix: list[list[int]], expected: list[list[int]]):
        self.solution.rotate(matrix)
        assert matrix == expected
