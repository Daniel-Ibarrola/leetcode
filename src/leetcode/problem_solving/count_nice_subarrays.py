class Solution:
    @staticmethod
    def count_nice_subarrays(nums: list[int], k: int) -> int:
        num_nice_subarrays = 0
        for ii in range(len(nums)):
            odd_count = 0
            for jj in range(ii, len(nums)):
                if nums[jj] % 2 == 1:
                    odd_count += 1

                if odd_count == k:
                    num_nice_subarrays += 1

                if odd_count > k:
                    break

        return num_nice_subarrays
