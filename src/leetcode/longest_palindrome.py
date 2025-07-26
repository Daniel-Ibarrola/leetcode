class Solution:
    @staticmethod
    def longest_palindrome(words: list[str]) -> int:
        word_count: dict[str, int] = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        current_length: int = 0
        already_palindrome: bool = False

        for word in words:
            reversed_word = word[::-1]
            count = word_count[word]

            if word == reversed_word:

                if count == 0:
                    continue

                if count == 1 and not already_palindrome:
                    current_length += 1
                    already_palindrome = True
                    word_count[word] = 0
                else:
                    occurrences_to_use = count - count % 2
                    current_length += occurrences_to_use
                    word_count[word] = count - occurrences_to_use

            else:
                # We have found a pair that can form part of a palindrome (e.g) "ab", "ba"
                reversed_count = word_count.get(reversed_word, 0)
                if reversed_count > 0 and count > 0:
                    current_length += 2
                    word_count[reversed_word] -= 1
                    word_count[word] -= 1

        return current_length * 2
