
def is_palindrome(string: str) -> bool:
    left = 0
    right = len(string) - 1

    while left < right:
        left_char = string[left].lower()
        right_char = string[right].lower()

        if not left_char.isalnum():
            left += 1
            continue

        if not right_char.isalnum():
            right -= 1
            continue

        if left_char != right_char:
            return False

        left += 1
        right -= 1

    return True
