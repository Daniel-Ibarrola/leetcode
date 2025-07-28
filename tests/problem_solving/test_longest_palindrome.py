import pytest

from leetcode.problem_solving.longest_palindrome import Solution


class TestLongestPalindrome:
    solution = Solution()

    @pytest.mark.parametrize(
        "words,expected",
        [
            (["lc", "cl", "gg"], 6),
            (["ab", "ty", "yt", "lc", "cl", "ab"], 8),
            (["cc", "ll", "xx"], 2),
            (["ab"], 0),
            (["em", "pe", "mp", "ee", "pp", "me", "ep", "em", "em", "me"], 14),
        ],
    )
    def test_finds_longest_palindrome_length(self, words: list[str], expected: int):
        assert self.solution.longest_palindrome(words) == expected

    def test_find_longest_palindrome_length_with_empty_list(self):
        assert self.solution.longest_palindrome([]) == 0

    @pytest.mark.parametrize(
        "words,expected",
        [
            (["aa", "aa"], 4),
            (["ab", "ab", "ba", "ba"], 8),
            (
                [
                    "dd",
                    "aa",
                    "bb",
                    "dd",
                    "aa",
                    "dd",
                    "bb",
                    "dd",
                    "aa",
                    "cc",
                    "bb",
                    "cc",
                    "dd",
                    "cc",
                ],
                22,
            ),
        ],
    )
    def test_find_longest_palindrome_when_words_are_not_unique(
        self, words: list[str], expected: int
    ):
        assert self.solution.longest_palindrome(words) == expected
