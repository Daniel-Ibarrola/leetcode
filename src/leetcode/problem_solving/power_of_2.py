from collections import Counter


def find_pairs(nums: list[int]) -> int:
    power_of_twos = [1 << i for i in range(32)]  # 2^0 to 2^31
    count = 0
    freq = Counter()

    for num in nums:
        freq[num] += 1
        for target_sum in power_of_twos:
            complement = target_sum - num
            count += freq[complement]

    return count
