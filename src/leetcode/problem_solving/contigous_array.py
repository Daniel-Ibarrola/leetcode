class Solution:
    @staticmethod
    def find_max_length(nums: list[int]) -> int:
        max_length = 0

        for ii in range(len(nums)):
            for jj in range(ii + 1, len(nums)):
                subarray = nums[ii : jj + 1]
                nums_zeros = subarray.count(0)
                num_ones = len(subarray) - nums_zeros

                if num_ones == nums_zeros:
                    max_length = max(max_length, len(subarray))

        return max_length
