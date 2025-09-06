import pytest

from leetcode.basic.array_pair_sum import array_pair_sum


@pytest.mark.parametrize(
    "nums, expected",
    [
        # Example cases
        ([1, 4, 3, 2], 4),
        ([6, 2, 6, 5, 1, 2], 9),
        # Edge cases
        ([1, 2], 1),  # Only one pair possible
        ([0, 0], 0),  # Pairing zeros
        # Larger case
        ([9, 8, 7, 6, 5, 4, 3, 2], 20),  # Optimal: (2,3),(4,5),(6,7),(8,9) → 2+4+6+8=20
    ],
)
def test_array_pair_sum(nums, expected):
    assert array_pair_sum(nums) == expected
