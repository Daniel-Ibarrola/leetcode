def array_pair_sum(nums: list[int]) -> int:
    nums.sort()
    sum_ = 0
    for ii in range(0, len(nums), 2):
        sum_ += nums[ii]
    return sum_
