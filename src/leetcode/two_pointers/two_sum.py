def has_pair_sum(nums: list[int], target: int) -> bool:
    """Given a sorted array nums and a target value, return true if there is a pair in nums whose sum is equal to the target.

    :param nums: a sorted array of integers
    :param target: the target value
    :return: boolean indicating whether there is a pair in nums whose sum is equal to the target
    """
    left, right = 0, len(nums) - 1
    while left < right:
        sum_ = nums[left] + nums[right]
        if sum_ == target:
            return True
        elif sum_ < target:
            left += 1
        else:
            right -= 1

    return False
