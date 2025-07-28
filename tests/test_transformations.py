import pytest
from leetcode.transformations import transform_array  # adjust import as needed


@pytest.mark.parametrize(
    "arr, expected",
    [
        # Basic case
        ([1, 2, 3], [3, 6, 5]),
        ([4, 0, 1, -2, 3], [4, 5, -1, 2, 1]),
        # Single element
        ([10], [10]),
        # Two elements
        ([4, 5], [9, 9]),
        # With negative numbers
        ([2, -1, 3], [1, 4, 2]),
        # All zeros
        ([0, 0, 0, 0], [0, 0, 0, 0]),
        # Increasing sequence
        ([1, 2, 3, 4, 5], [3, 6, 9, 12, 9]),
        # Decreasing sequence
        ([5, 4, 3, 2, 1], [9, 12, 9, 6, 3]),
        # Edge case: empty input
        ([], []),
    ],
)
def test_transform_array(arr: list[int], expected: list[int]):
    assert transform_array(arr) == expected
