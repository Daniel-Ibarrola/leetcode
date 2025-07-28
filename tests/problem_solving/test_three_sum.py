import pytest

from leetcode.problem_solving.three_sum import Solution


class TestThreeSumWithMultiplicity:
    solution = Solution()

    @pytest.mark.parametrize(
        "nums,target,expected",
        [
            ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8, 20),
            ([1, 1, 2, 2, 2, 2], 5, 12),
            ([2, 1, 3], 6, 1),
        ],
    )
    def test_calculates_correct_number_of_triples(
        self, nums: list[int], target: int, expected: int
    ):
        assert self.solution.three_sum_with_multiplicity(nums, target) == expected
