import pytest

from leetcode.num_pairs_divisible_by_60 import Solution


class TestNumPairsDivisibleBy60:

    solution = Solution()

    @pytest.mark.parametrize(
        "time,expected", [([30, 20, 150, 100, 40], 3), ([60, 60, 60], 3), ([20, 40], 1)]
    )
    def test_finds_pairs(self, time: list[int], expected: int):
        assert self.solution.num_pairs_divisible_by_60(time) == expected
