import pytest
from leetcode.prefix_sum.count_vowel_sub_strings import Solution


class TestCountVowelStrings:
    solution = Solution()

    @pytest.mark.parametrize(
        "word, queries, expected",
        [
            # Example cases
            ("prefixsum", [[0, 2], [1, 4], [3, 5]], [1, 2, 1]),
        ],
    )
    def test_count_vowel_substrings(
        self, word: str, queries: list[list[int]], expected: list[int]
    ):
        assert self.solution.vowel_strings(word, queries) == expected
