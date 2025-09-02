from leetcode.sliding_window.max_sum_of_subarray import (
    max_sum_of_subarray,
)


def test_example_case():
    assert max_sum_of_subarray([2, 1, 5, 1, 3, 2], 3) == 9  # [5,1,3]


def test_subarray_size_1():
    assert max_sum_of_subarray([2, 1, 5, 1, 3, 2], 1) == 5  # just max element


def test_entire_array():
    assert max_sum_of_subarray([2, 1, 5, 1, 3, 2], 6) == sum([2, 1, 5, 1, 3, 2])


def test_multiple_equal_max_subarrays():
    # max sum subarrays: [2,2,2] and [2,2,2], sum = 6
    assert max_sum_of_subarray([2, 2, 2, 2, 2], 3) == 6


def test_mixed_numbers():
    # best window is [4,5] with sum 9
    assert max_sum_of_subarray([1, -1, 4, 5, -2, 3], 2) == 9


def test_subarray_size_equals_list_length():
    assert max_sum_of_subarray([10, -2, 3], 3) == 11  # whole array


def test_single_element_array():
    assert max_sum_of_subarray([7], 1) == 7


def test_large_k_on_small_array():
    nums = [1, 2]
    k = 2
    assert max_sum_of_subarray(nums, k) == 3
