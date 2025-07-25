class Solution:
    @staticmethod
    def longest_palindrome(words: list[str]) -> int:
        words_set: set[str] = set(words)

        current_length: int = 0
        found_self_palindrome: bool = False

        for word in words:
            reversed_word = word[::-1]

            if not found_self_palindrome and word == reversed_word:
                current_length += 2
                # words_set.remove(word)
                found_self_palindrome = True
                continue
            elif word == reversed_word:
                # words_set.remove(word)
                continue

            # We have found a pair that can form part of a palindrome (e.g) "ab", "ba"
            if reversed_word in words_set:
                current_length += 4
                words_set.remove(reversed_word)
                words_set.remove(word)

        return current_length
