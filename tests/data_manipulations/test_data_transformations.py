import pytest
from leetcode.data_manipulations.data_manipulation import check_for_pattern


@pytest.mark.parametrize(
    "pattern, source, expected",
    [
        # Example from the description
        ("010", "amazing", 2),
        ("100", "codesignal", 0),
        # All vowels
        ("000", "aeiouy", 4),  # "aei", "eio", "iou", "ouy"
        # All consonants
        ("111", "bcdfgh", 4),  # "bcd", "cdf", "dfg", "fgh"
        # Alternating pattern with mix input
        ("0101", "banana", 1),  # "anan" matches
        # Pattern longer than source
        ("01", "a", 0),
        # Pattern and source are the same length
        ("01", "an", 1),  # "an" matches: 0=a (vowel), 1=n (consonant)
        ("01", "na", 0),  # "na" does not match
        # Edge case: pattern length == 1
        ("0", "aeiouybcdfgh", 6),  # 6 vowels
        ("1", "aeiouybcdfgh", 6),  # 6 consonants
        # Edge case: source full of same letter
        ("000", "aaaaaaa", 5),  # a is vowel, so 5 substrings of length 3
        ("111", "bbbbbbb", 5),  # same but consonants
        # No matching substrings
        ("01", "zzz", 0),
        # Full match
        ("010101", "abecid", 1),
        # Long input with repeating pattern
        ("01" * 5, "ab" * 10, 6),  # Pattern: 0101010101, Source: abababababababababab
    ],
)
def test_solution(pattern, source, expected):
    assert check_for_pattern(pattern, source) == expected
