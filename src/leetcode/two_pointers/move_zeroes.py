def move_zeroes(nums: list[int]) -> None:
    new_index = 0
    for index in range(len(nums)):
        if nums[index] != 0:
            nums[new_index] = nums[index]
            new_index += 1

    for index in range(new_index, len(nums)):
        nums[index] = 0
