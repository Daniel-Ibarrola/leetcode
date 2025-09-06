def sort_colors(nums: list[int]) -> None:
    zeros_count = 0
    ones_count = 0
    twos_count = 0

    for num in nums:
        if num == 0:
            zeros_count += 1
        elif num == 1:
            ones_count += 1
        else:
            twos_count += 1

    for ii in range(zeros_count):
        nums[ii] = 0

    for ii in range(zeros_count, zeros_count + ones_count):
        nums[ii] = 1

    for ii in range(zeros_count + ones_count, len(nums)):
        nums[ii] = 2
