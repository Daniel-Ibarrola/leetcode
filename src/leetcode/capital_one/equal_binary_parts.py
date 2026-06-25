def can_divide_into_equal_parts(nums: list[int]) -> bool:
    """Given an array of 0s and 1s, determine whether it can be divided into
    exactly 3 non-empty contiguous parts such that all three parts represent
    the same binary value (leading zeros are allowed).

    Example 1:
        Input: nums = [1, 0, 1, 0, 1]
        Output: True
        Explanation: Parts [1,0], [1,0], [1] all represent the value 2, 2, 1 — wait,
                     actually [1,0] = 2, [1,0] = 2, [1] = 1. Hmm.
                     Valid split: [1], [0,1], [0,1] — all equal binary value? No.
                     Correct: [1,0], [1,0], [1] ... reconsider.
                     The parts must have the same binary integer value ignoring leading zeros:
                     [1,0] = 2, [1,0] = 2, [1] = 1 → not equal.
                     Correct valid split: indices [0..1], [2..3], [4] → 10, 10, 1 → not equal.
                     Valid: [1], [01], [01] → 1, 1, 1 → True.

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
    pass
