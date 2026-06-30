def can_divide_into_equal_parts(nums: list[int]) -> bool:
    """Given an array of 0s and 1s, determine whether it can be divided into
    exactly 3 non-empty contiguous parts such that all three parts represent
    the same binary value (leading zeros are allowed).

    Example 1:
        Input: nums = [1, 0, 1, 0, 1]
        Output: True
        Explanation: Valid: [1], [01], [01] → 1, 1, 1 → True.

    Example 2:
        Input: nums = [1, 1, 0, 1, 1]
        Output: False
        Explanation: Total number of 1s is 4, which is not divisible by 3.

    Example 3:
        Input: nums = [0, 0, 0]
        Output: True
        Explanation: [0], [0], [0] all represent the value 0.

    Constraints:
        - 3 <= len(nums) <= 3 * 10^4
        - nums[i] is either 0 or 1

    :param nums: list of 0s and 1s
    :return: True if the array can be split into 3 parts with equal binary value
    """
    ones = [i for i, x in enumerate(nums) if x == 1]

    if len(ones) == 0:
        return True
    if len(ones) % 3 != 0:
        return False

    k = len(ones) // 3
    i1, i2, i3 = ones[0], ones[k], ones[2 * k]

    # Compare all three segments simultaneously; third segment ends at n-1
    while i3 < len(nums):
        if nums[i1] != nums[i2] or nums[i2] != nums[i3]:
            return False
        i1 += 1
        i2 += 1
        i3 += 1

    # i1 and i2 must not have run into the next segment's territory
    return i1 <= i2 <= i3
