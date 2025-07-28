class Solution:
    """
    Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

    A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

    Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

    Example 1:

    Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
    Output: ["mee","aqq"]
    Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
    "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
    Example 2:

    Input: words = ["a","b","c"], pattern = "a"
    Output: ["a","b","c"]

    """

    @staticmethod
    def match_pattern(pattern: str, word: str) -> bool:
        pattern_mappings: dict[str, str] = {}
        word_mappings: dict[str, str] = {}
        for ii in range(len(pattern)):
            pattern_char = pattern[ii]
            word_char = word[ii]

            pattern_mapping = pattern_mappings.get(pattern_char)
            word_mapping = word_mappings.get(word_char)

            if pattern_mapping is None:
                pattern_mappings[pattern_char] = word_char

            if word_mapping is None:
                word_mappings[word_char] = pattern_char

            if pattern_char != word_mapping and word_mapping != pattern_mapping:
                return False

        return True

    def find_and_replace_pattern(self, words: list[str], pattern: str) -> list[str]:
        matches: list[str] = []

        for word in words:
            is_match = self.match_pattern(pattern, word)
            if is_match:
                matches.append(word)

        return matches
