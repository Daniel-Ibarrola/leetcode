from collections import defaultdict


class Solution:
    @staticmethod
    def subarray_sum(nums: list[int], target: int) -> int:
        """Returns the number of subarrays with sum equals to target

        :param nums: an array of integers
        :param target: the target sum
        :return: the number of subarrays with sum equals to target
        """
        prefix_sums = defaultdict(int)
        count = 0

        for ii in range(len(nums)):
            prefix_sums[ii] = prefix_sums[ii - 1] + nums[ii]

        return count
