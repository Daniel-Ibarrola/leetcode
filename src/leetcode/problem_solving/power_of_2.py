def find_pairs(nums: list[int]) -> int:
    count = 0

    for ii in range(len(nums)):
        for jj in range(ii, len(nums)):
            pair_sum = nums[ii] + nums[jj]
            if pair_sum > 0 and (pair_sum & (pair_sum - 1)) == 0:
                count += 1

    return count
