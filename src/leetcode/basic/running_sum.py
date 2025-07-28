class Solution:
    @staticmethod
    def running_sum(nums: list[int]) -> list[int]:
        if not nums:
            return []

        sums: list[int] = [0] * len(nums)
        sums[0] = nums[0]

        for ii in range(1, len(nums)):
            sums[ii] = sums[ii - 1] + nums[ii]

        return sums
