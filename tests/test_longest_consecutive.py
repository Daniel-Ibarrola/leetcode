from leetcode.longest_consecutive_sequence import Solution
from pytest import mark


class TestLongestConsecutive:
    solution = Solution()

    @mark.parametrize(
        "nums,expected",
        [
            ([100, 4, 200, 1, 3, 2], 4),
            ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
            ([1, 0, 1, 2], 3),
            ([1, 2, 3, 4, 5], 5),
            ([1, 1, 1], 1),
        ],
    )
    def test_longest_consecutive(self, nums: list[int], expected: int):
        assert self.solution.longest_consecutive(nums) == expected
