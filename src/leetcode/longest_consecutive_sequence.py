class Solution:

    @staticmethod
    def longest_consecutive(nums: list[int]) -> int:
        unique_nums: set[int] = set(nums)
        current_max: int = 0
        for num in unique_nums:
            if num - 1 not in unique_nums:
                current_num = num + 1
                while current_num in unique_nums:
                    current_num += 1

                current_max = max(current_max, current_num - num)

        return current_max
