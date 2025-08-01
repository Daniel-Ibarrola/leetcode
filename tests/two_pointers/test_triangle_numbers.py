import pytest
from leetcode.two_pointers.triangle_numbers import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        # Basic cases
        ([2, 2, 3, 4], 3),  # Three valid triangles: [2,3,4] x2 and [2,2,3]
        ([4, 2, 3, 4], 4),  # Four valid triangles
        # Edge cases
        ([0, 0, 0], 0),  # All sides are zero, no triangle possible
        ([1, 1, 2], 0),  # 1 + 1 = 2, not greater than 2 → invalid
        ([1, 2, 3], 0),  # 1 + 2 = 3 → not valid
        # All sides same
        ([3, 3, 3], 1),  # Only one triangle possible
        # Larger input
        ([2, 2, 2, 2], 4),  # Four combinations: choose any 3 out of 4 → C(4,3) = 4
        # Mixed valid/invalid
        ([10, 21, 22, 100, 101, 200, 300], 6),  # Various combinations possible
        # Single or two elements
        ([5], 0),
        ([5, 6], 0),
        # Long input, all valid
        ([5] * 50, 19600),  # C(50, 3) = 19600 triangles when all values are the same
    ],
)
def test_triangle_number(nums: list[int], expected: int):
    assert Solution().triangle_number(nums) == expected
