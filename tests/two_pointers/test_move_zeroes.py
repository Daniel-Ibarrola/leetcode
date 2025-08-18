import pytest
from leetcode.two_pointers.move_zeroes import move_zeroes


@pytest.mark.parametrize(
    "nums, expected",
    [
        # Example 1
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        # Example 2
        ([0], [0]),
        # No zeroes
        ([1, 2, 3], [1, 2, 3]),
        # All zeroes
        ([0, 0, 0, 0], [0, 0, 0, 0]),
        # Zeroes at beginning
        ([0, 0, 1, 2, 3], [1, 2, 3, 0, 0]),
        # Zeroes at end (already valid)
        ([1, 2, 3, 0, 0], [1, 2, 3, 0, 0]),
        # Alternating zeroes
        ([0, 1, 0, 2, 0, 3], [1, 2, 3, 0, 0, 0]),
        # Negative numbers with zeroes
        ([0, -1, 0, -2, 3], [-1, -2, 3, 0, 0]),
        # Large numbers with zeroes
        ([0, 1000000, 0, 5], [1000000, 5, 0, 0]),
        # Single element non-zero
        ([7], [7]),
    ],
)
def test_move_zeroes(nums, expected):
    move_zeroes(nums)  # modifies in-place
    assert nums == expected
