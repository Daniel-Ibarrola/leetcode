from black.trans import defaultdict


class Solution:
    @staticmethod
    def subarray_sum(nums: list[int], k: int) -> int:
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1

        current_sum = 0
        count = 0
        for num in nums:
            current_sum += num
            count += prefix_counts[current_sum - k]
            prefix_counts[current_sum] += 1

        return count
