from leetcode.problem_solving.four_sum_count import Solution


class TestFourSumCount:
    solution = Solution()

    def test_finds_correct_number_of_tuples(self):
        nums1 = [1, 2]
        nums2 = [-2, -1]
        nums3 = [-1, 2]
        nums4 = [0, 2]
        assert self.solution.four_sum_count(nums1, nums2, nums3, nums4) == 2

    def all_arrays_are_the_same(self):
        assert self.solution.four_sum_count([0], [0], [0], [0]) == 1
