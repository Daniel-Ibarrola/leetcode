from leetcode.longest_alternating_subarray import Solution


class TestLongestAlternatingSubarray:

    solution = Solution()

    def test_case_1(self):
        assert self.solution.alternating_subarray([2, 3, 4, 3, 4]) == 4

    def test_case_2(self):
        assert self.solution.alternating_subarray([4, 5, 6]) == 2
