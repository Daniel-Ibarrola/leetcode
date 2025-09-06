import pytest
from leetcode.basic.sort_by_parity import sort_by_parity, sort_by_parity_2


@pytest.mark.parametrize(
    "nums,expected_options",
    [
        # Example 1: mixed even and odd
        ([3, 1, 2, 4], [[2, 4, 3, 1], [4, 2, 3, 1], [2, 4, 1, 3], [4, 2, 1, 3]]),
        # Example 2: single element (edge case)
        ([0], [[0]]),
        # All even numbers (should remain unchanged, but any permutation is valid)
        ([2, 4, 6, 8], [[2, 4, 6, 8], [8, 6, 4, 2]]),
        # All odd numbers (should remain unchanged, but order doesn’t matter)
        ([1, 3, 5, 7], [[1, 3, 5, 7], [7, 5, 3, 1]]),
        # Even numbers first, odds last (already sorted by parity)
        ([2, 4, 1, 3], [[2, 4, 1, 3], [4, 2, 1, 3]]),
        # Odds first, evens last (should reorder)
        ([1, 3, 2, 4], [[2, 4, 1, 3], [4, 2, 1, 3]]),
        # Single odd number
        ([5], [[5]]),
        # Mixture with zero (even)
        ([0, 1, 2, 3], [[0, 2, 1, 3], [2, 0, 1, 3]]),
        # Larger array, mixed values
        ([9, 2, 5, 6, 3, 8], [[2, 6, 8, 9, 5, 3], [8, 6, 2, 9, 5, 3]]),
    ],
)
def test_sort_array_by_parity(nums, expected_options):
    result = sort_by_parity(nums)
    # Verify all evens come before odds
    split_index = 0
    while split_index < len(result) and result[split_index] % 2 == 0:
        split_index += 1
    assert all(x % 2 == 1 for x in result[split_index:])
    # Also check result is one of the acceptable permutations
    assert result in expected_options


def is_valid_parity_arrangement(nums: list[int]) -> bool:
    """Helper to check if even indices have even numbers and odd indices have odd numbers."""
    return all(
        (i % 2 == 0 and nums[i] % 2 == 0) or (i % 2 == 1 and nums[i] % 2 == 1)
        for i in range(len(nums))
    )


@pytest.mark.parametrize(
    "nums",
    [
        # Example cases
        [4, 2, 5, 7],
        [2, 3],
        # Edge cases (smallest possible input)
        [0, 1],
        [2, 3],
        # Already valid
        [2, 5, 4, 7],
        [0, 1, 2, 3],
        # Reverse parity order
        [1, 2, 3, 4],
        [5, 2, 7, 4],
        # Larger random cases
        [2, 3, 4, 5, 6, 7],
        [10, 1, 12, 3, 14, 5],
        [1000, 999, 888, 777, 222, 111],
    ],
)
def test_sort_array_by_parity_ii(nums):
    result = sort_by_parity_2(nums)
    # Check length preserved
    assert len(result) == len(nums)
    # Check that result is a permutation of input
    assert sorted(result) == sorted(nums)
    # Check parity condition
    assert is_valid_parity_arrangement(result)
