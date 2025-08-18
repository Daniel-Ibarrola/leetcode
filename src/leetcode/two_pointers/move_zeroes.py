def move_zeroes(nums: list[int]) -> None:
    new_nums: list[int] = [0] * len(nums)

    new_nums_index = 0
    for nums_index in range(len(nums)):
        if nums[nums_index] != 0:
            new_nums[new_nums_index] = nums[nums_index]
            new_nums_index += 1

    nums[:] = new_nums
