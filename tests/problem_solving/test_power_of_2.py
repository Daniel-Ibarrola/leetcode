import pytest
from leetcode.problem_solving.power_of_2 import find_pairs


@pytest.mark.parametrize(
    "numbers, expected",
    [
        # Examples from the problem description
        ([1, -1, 2, 3], 5),
        ([2], 1),
        ([-2, -1, 0, 1, 2], 5),
        # All elements are powers of two
        ([1, 2, 4, 8], 4),  # (0,0)=2, (1,1)=4, (2,2)=8, (3,3)=16
        # All elements are negative
        ([-1, -2, -4], 0),  # No pair will sum to a power of 2
        # Includes large positive and negative values
        (
            [1024, -1023, -1, 0],
            3,
        ),  # 1024 + (-1023)=1, -1 + 1 = 0 (not power of 2), 0+0 = 0 (not power of 2), etc.
        # Edge case: duplicates are not allowed, but test edge behavior
        (
            [0, 1, 3, 5, 7],
            5,
        ),  # (0,1)=1,(1,1)=2,(1,3)=4,(1,7)=8,(3,5)=8,
        (
            [0, 1, 2, 3, 5],
            6,
        ),  # (0,1)=1, (0,2)=2, (1,1)=2, (1,3)=4, (2,2)=4, (3,5) = 8
        # Single large power of 2
        ([2**20], 1),  # Self-pair: (0, 0)
    ],
)
def test_solution(numbers, expected):
    assert find_pairs(numbers) == expected
