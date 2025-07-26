class Solution:
    @staticmethod
    def num_pairs_divisible_by_60(time: list[int]) -> int:
        remainders_counts = [0] * 60
        for t in time:
            remainders_counts[t % 60] += 1

        num_pairs = remainders_counts[0] * (remainders_counts[0] - 1) // 2
        num_pairs += remainders_counts[30] * (remainders_counts[30] - 1) // 2

        for ii in range(1, 30):
            num_pairs += remainders_counts[ii] * remainders_counts[60 - ii]

        return num_pairs
