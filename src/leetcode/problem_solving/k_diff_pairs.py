from collections import Counter


class Solution:
    @staticmethod
    def find_pairs(nums: list[int], k: int) -> int:
        count = 0
        frequency = Counter(nums)
        if k == 0:
            # Look for repeated numbers e.g (1, 1), (2, 2)
            for num, freq in frequency.items():
                if freq > 1:
                    count += 1
        else:
            for num, freq in frequency.items():
                if num + k in frequency:
                    count += 1

        return count
