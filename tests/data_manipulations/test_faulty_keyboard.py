import pytest
from leetcode.data_manipulations.faulty_keyboard import Solution


class TestFaultyKeyboard:
    solution = Solution()

    @pytest.mark.parametrize(
        "string, expected",
        [
            # Example cases
            ("string", "rtsng"),
            ("poiinter", "ponter"),
            # Edge cases
            ("a", "a"),  # Single non-'i' char
            ("i", ""),  # Should reverse empty string => still empty
            ("ii", ""),  # Reverse empty -> empty twice
            # Strings with multiple 'i' reversals
            ("abciidef", "abcdef"),  # double reverse brings back to original
            ("abcdiiefg", "abcdefg"),  # double i resets
            # No i at all
            ("keyboard", "keyboard"),
            # All i's
            ("iiii", ""),  # all i's reverse empty string repeatedly
            # Starts with multiple letters and ends with i
            ("helloi", "olleh"),
            # Alternating i's
        ],
    )
    def test_faulty_keyboard(self, string: str, expected: str):
        assert self.solution.final_string(string) == expected
