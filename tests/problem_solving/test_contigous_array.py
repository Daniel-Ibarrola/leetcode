import pytest
from leetcode.problem_solving.contigous_array import Solution


class TestContiguousArray:
    solution = Solution()

    @pytest.mark.parametrize(
        "nums, expected",
        [
            # Example cases
            ([0, 1], 2),
            ([0, 1, 0], 2),
            ([0, 1, 1, 1, 1, 1, 0, 0, 0], 6),
            # Edge case: alternating 0s and 1s
            ([0, 1, 0, 1, 0, 1], 6),
            # Edge case: no equal 0s and 1s
            ([0, 0, 0, 0], 0),
            ([1, 1, 1, 1], 0),
            # Edge case: equal count, entire array
            ([0, 0, 1, 1], 4),
            ([1, 1, 0, 0], 4),
            # Longer subarray in the middle
            (
                [1, 0, 1, 1, 1, 0, 0],
                6,
            ),  # [1, 1, 1, 0, 0] is length 5; best is [0,1,1,1,0,0]
            # Minimum input size
            ([0], 0),
            ([1], 0),
        ],
    )
    def test_find_max_length(self, nums, expected):
        assert self.solution.find_max_length(nums) == expected
