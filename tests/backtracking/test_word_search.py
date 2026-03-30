import pytest
from src.leetcode.backtracking.word_search import check_word_exists


@pytest.mark.parametrize(
    "board, word, expected",
    [
        # Example 1: Positive case (BLEAK)
        (
            [
                ["B", "L", "C", "H"],
                ["D", "E", "L", "T"],
                ["D", "A", "K", "A"],
            ],
            "BLEAK",
            True,
        ),
        # Example 2: Negative case (BLEED)
        (
            [
                ["B", "L", "C", "H"],
                ["D", "E", "L", "T"],
                ["D", "A", "K", "A"],
            ],
            "BLEED",
            False,
        ),
        # Additional cases:
        # Single character board - match
        ([["A"]], "A", True),
        # Single character board - no match
        ([["A"]], "B", False),
        # Multi-path search (to check backtracking)
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCCED",
            True,
        ),
        # Case with reused letter (should be False)
        ([["A", "B"], ["C", "D"]], "ABCDA", False),
        # Word longer than board size
        ([["A"]], "AB", False),
        # Empty string (should return True? usually empty word is considered exists, or depends on requirements.
        # Usually problem states word length >= 1, but let's assume it should match if it's there.
        # But for Word Search, let's stick to non-empty strings as per typical LeetCode.)
        ([["A", "B"], ["C", "D"]], "ACDB", True),
        # Snake path
        ([["A", "B", "C"], ["F", "E", "D"], ["G", "H", "I"]], "ABCDEFGHI", True),
    ],
)
def test_check_word_exists(board, word, expected):
    assert check_word_exists(board, word) == expected
