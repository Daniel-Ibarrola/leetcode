import pytest
from leetcode.sliding_window.longest_unique_substring import (
    Solution,
)  # Replace with your actual import


class TestLongestSubstringWithoutRepeats:
    solution = Solution()

    @pytest.mark.parametrize(
        "string, expected",
        [
            # Example cases
            ("abcabcbb", 3),  # "abc"
            ("bbbbb", 1),  # "b"
            ("pwwkew", 3),  # "wke"
            # Edge cases
            ("", 0),  # Empty string
            ("a", 1),  # Single character
            ("abcdefg", 7),  # All unique characters
            ("abba", 2),  # "ab" or "ba"
            ("tmmzuxt", 5),  # "mzuxt"
            # Repeating every other character
            ("abababab", 2),  # "ab"
            # Numbers and symbols
            ("1234567890", 10),  # All unique
            ("a1b2c3d4e5", 10),  # All unique
            # Upper/lowercase distinction
            ("AaBbCc", 6),  # case-sensitive
            # Long repeating string
            ("a" * 1000, 1),
            # Longer mixed string
            ("dvdf", 3),  # "vdf"
        ],
    )
    def test_length_of_longest_substring(self, string: str, expected: int):
        assert self.solution.length_of_longest_substring(string) == expected
