import pytest

from leetcode.spiral_order import Solution


class TestSpiralOrder:

    solution = Solution()

    @pytest.mark.parametrize(
        "matrix,expected",
        [
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
            (
                [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
            ),
            ([[7], [9], [6]], [7, 9, 6]),
            (
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16],
                    [17, 18, 19, 20],
                    [21, 22, 23, 24],
                ],
                [
                    1,
                    2,
                    3,
                    4,
                    8,
                    12,
                    16,
                    20,
                    24,
                    23,
                    22,
                    21,
                    17,
                    13,
                    9,
                    5,
                    6,
                    7,
                    11,
                    15,
                    19,
                    18,
                    14,
                    10,
                ],
            ),
        ],
    )
    def test_outputs_matrix_in_spiral_order(
        self, matrix: list[list[int]], expected: list[int]
    ):
        assert self.solution.spiral_order(matrix) == expected
