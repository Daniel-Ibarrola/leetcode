import pytest
from leetcode.sliding_window.character_replacement import character_replacement


@pytest.mark.parametrize(
    "string, replacement_times, expected",
    [
        # ✅ Examples from the problem statement
        ("ABAB", 2, 4),  # replace 2 A's or 2 B's → "BBBB" or "AAAA"
        ("AABABBA", 1, 4),  # replace middle 'A' → "AABBBBA" → longest "BBBB"
        # 🔹 Edge cases
        ("A", 0, 1),  # single char, no replacement
        ("A", 1, 1),  # single char, replacement doesn't help
        ("AB", 0, 1),  # no replacement, only single char substrings
        ("AB", 1, 2),  # replace one → "AA" or "BB"
        # 🔹 All characters the same
        ("AAAA", 0, 4),  # no replacement needed
        ("AAAA", 2, 4),  # already uniform
        # 🔹 Alternating characters
        ("ABABABAB", 2, 5),  # replace 2 → "AAAAA" or "BBBBB"
        ("ABABABAB", 3, 7),  # replace 3 → "AAAAAA" or "BBBBBB"
        # 🔹 Larger k than needed
        ("ABCDE", 10, 5),  # can replace all to same → whole string
        # 🔹 Complex mix
        ("BAAAB", 2, 5),  # replace 2 B's → "AAAAA"
        ("AAABBC", 2, 5),  # replace BB → "AAAAA"
        # 🔹 Long string
        ("ABBBACCCDDDD", 2, 6),  # "DDDDDD"
    ],
)
def test_character_replacement(string: str, replacement_times: int, expected: int):
    assert character_replacement(string, replacement_times) == expected
