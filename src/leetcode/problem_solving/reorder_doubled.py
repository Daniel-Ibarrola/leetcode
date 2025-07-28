from collections import Counter


class Solution:
    @staticmethod
    def can_reorder_doubled(arr: list[int]) -> bool:
        frequency = Counter(arr)
        for num in sorted(frequency, key=abs):
            if frequency[num] > frequency[2 * num]:
                return False

            frequency[2 * num] -= frequency[num]

        return True
