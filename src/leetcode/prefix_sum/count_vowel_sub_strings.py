from collections import defaultdict


class Solution:
    @staticmethod
    def vowel_strings(word: str, queries: list[list[int]]) -> list[int]:
        vowels = {"a", "e", "i", "o", "u"}
        prefix_vowel_counts = defaultdict(int)

        for ii in range(len(word)):
            vowel = 0 if word[ii] not in vowels else 1
            prefix_vowel_counts[ii] = prefix_vowel_counts[ii - 1] + vowel

        query_results: list[int] = []
        for [start, end] in queries:
            query_results.append(prefix_vowel_counts[end] - prefix_vowel_counts[start])

        return query_results
