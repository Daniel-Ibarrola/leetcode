def max_sum_of_subarray(nums: list[int], subarray_size: int) -> int:
    subarray_sum = sum(nums[0:subarray_size])
    current_max = subarray_sum

    for start in range(len(nums) - subarray_size):
        subarray_sum -= nums[start]
        subarray_sum += nums[start + subarray_size]
        current_max = max(current_max, subarray_sum)

    return current_max
