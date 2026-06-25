
def length_of_longest_substring(string: str) -> int:
    """ Returns the length of the longest substring in the given string"""
    seen: set[str] = set()

    left = 0
    max_len = 0
    for right in range(len(string)):
        char = string[right]

        while char in seen:
            seen.remove(string[left])
            left += 1

        seen.add(char)
        max_len = max(max_len, right - left + 1)

    return max_len