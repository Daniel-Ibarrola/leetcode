import pytest
from leetcode.two_pointers.is_palindrome import is_palindrome


@pytest.mark.parametrize(
    "s, expected",
    [
        # Example cases
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("Was it a car or a cat I saw?", True),
        # Empty and whitespace-only (no alphanumeric chars)
        ("", True),
        (" ", True),
        (".,!", True),
        # Single alphanumeric character
        ("a", True),
        ("Z", True),
        # Case insensitivity
        ("Aba", True),
        ("AbBa", True),
        ("AbCba", True),
        # Numbers
        ("12321", True),
        ("12345", False),
        ("1 2 3 2 1", True),
        # Mixed alphanumeric with punctuation
        ("No 'x' in Nixon", True),
        ("0P", False),
        # Non-palindrome plain strings
        ("hello", False),
        ("racecar", True),
    ],
)
def test_is_palindrome(s: str, expected: bool):
    assert is_palindrome(s) == expected
