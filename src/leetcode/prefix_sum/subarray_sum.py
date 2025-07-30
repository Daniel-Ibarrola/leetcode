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
        prefix_sums[0] = 1

        count = 0
        current_sum = 0
        for num in nums:
            current_sum += num
            count += prefix_sums[current_sum - target]
            prefix_sums[current_sum] += 1

        return count
