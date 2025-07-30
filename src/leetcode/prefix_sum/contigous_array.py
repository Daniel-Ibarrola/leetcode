class Solution:
    @staticmethod
    def find_max_length(nums: list[int]) -> int:
        prefix_sum = {0: -1}  # maps cumulative sum to first index it was seen
        max_length = 0
        current_sum = 0

        for ii, num in enumerate(nums):
            current_sum += 1 if num == 1 else -1
            if current_sum in prefix_sum:
                max_length = max(max_length, ii - prefix_sum[current_sum])
            else:
                prefix_sum[current_sum] = ii

        return max_length
