import pytest

from leetcode.greedy.assign_cookies import find_content_children


@pytest.mark.parametrize(
    "greed_factor, size, expected",
    [
        # Example cases
        ([1, 2, 3], [1, 1], 1),
        ([1, 2], [1, 2, 3], 2),
        # All children can be satisfied
        ([1, 1, 1], [1, 1, 1], 3),
        ([1, 2, 3], [3, 3, 3], 3),
        # No cookie big enough
        ([5, 6, 7], [1, 2, 3], 0),
        # Equal number of cookies and children
        ([1, 2, 3], [1, 2, 3], 3),
        # More cookies than children
        ([1, 2], [1, 2, 2, 3], 2),
        # More children than cookies
        ([1, 2, 3, 4], [1, 2], 2),
        # Edge case: one child, one cookie, not enough
        ([5], [4], 0),
        # Edge case: one child, one cookie, just enough
        ([5], [5], 1),
        # Edge case: empty inputs
        ([], [], 0),
        ([1, 2, 3], [], 0),
        ([], [1, 2, 3], 0),
        ([10, 9, 8, 7], [5, 6, 7, 8], 2),
    ],
)
def test_find_content_children(greed_factor: list[int], size: list[int], expected: int):
    assert find_content_children(greed_factor, size) == expected
