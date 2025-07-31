class Solution:
    @staticmethod
    def length_of_longest_substring(string: str) -> int:
        largest = 0
        seen = set()

        start = 0
        for end in range(len(string)):
            char = string[end]

            while char in seen:
                seen.remove(string[start])
                start += 1

            seen.add(char)
            largest = max(largest, end - start + 1)

        return largest
