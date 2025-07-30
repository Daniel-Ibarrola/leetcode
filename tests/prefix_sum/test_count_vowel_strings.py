import pytest
from leetcode.prefix_sum.count_vowel_strings import Solution


class TestCountVowelStrings:
    solution = Solution()

    @pytest.mark.parametrize(
        "words, queries, expected",
        [
            # Example cases
            (["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1]], [2, 3, 0]),
            (["a", "e", "i"], [[0, 2], [0, 1], [2, 2]], [3, 2, 1]),
            # All non-vowel start/end
            (["bob", "dad", "cat"], [[0, 2], [1, 2]], [0, 0]),
            # Mixed case
            (
                ["apple", "orange", "grape", "egg", "umbrella", "ice"],
                [[0, 5], [2, 4], [3, 3]],
                [4, 2, 1],
            ),
            # Single word, edge index
            (["apple"], [[0, 0]], [1]),
            # Single word not vowel
            (["boat"], [[0, 0]], [0]),
            # Words of length 1
            (["a", "b", "e", "f", "i", "u", "z"], [[0, 6], [1, 5], [2, 4]], [4, 3, 2]),
            # Edge: full range, none match
            (["bravo", "delta", "echo"], [[0, 2]], [0]),
            # Edge: full range, all match
            (["a", "e", "i", "o", "u"], [[0, 4], [1, 3]], [5, 3]),
            # Edge case: query range is full and includes mixture
            (["a", "bee", "e", "car", "i"], [[0, 4]], [3]),
            # Query range overlap
            (
                ["apple", "eagle", "ear", "owl", "urge"],
                [[0, 2], [1, 4], [0, 4]],
                [3, 4, 5],
            ),
        ],
    )
    def test_count_vowel_strings(self, words, queries, expected):
        assert self.solution.vowel_strings(words, queries) == expected
