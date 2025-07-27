import pytest
from leetcode.generate_spiral_matrix import Solution


class TestGenerateSpiralMatrix:
    solution = Solution()

    @pytest.mark.parametrize(
        "size,expected", [(3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]), (1, [[1]])]
    )
    def test_generate_spiral_matrix(self, size: int, expected: list[list[int]]):
        assert self.solution.generate_spiral_matrix(size) == expected
