from leetcode.longest_alternating_subarray import Solution


class TestLongestAlternatingSubarray:

    solution = Solution()

    def test_finds_longest_alternating_subarray_1(self):
        assert self.solution.alternating_subarray([2, 3, 4, 3, 4]) == 4

    def test_finds_longest_alternating_subarray_2(self):
        assert self.solution.alternating_subarray([4, 5, 6]) == 2

    def test_no_alternating_subarrays(self):
        assert self.solution.alternating_subarray([1, 1, 1, 1]) == -1

    def test_whole_array_is_alternating(self):
        assert self.solution.alternating_subarray([2, 3, 2, 3, 2, 3]) == 6
