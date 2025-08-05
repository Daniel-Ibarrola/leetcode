from collections import defaultdict


def subarrays_sum_divisible_by_k(nums: list[int], k: int) -> int:
    prefixes = defaultdict(int)
    prefixes[0] = 1

    count = 0
    current_sum = 0
    for num in nums:
        current_sum += num
        mod = current_sum % k

        if mod < 0:
            mod += k

        count += prefixes[mod]
        prefixes[mod] += 1

    return count
