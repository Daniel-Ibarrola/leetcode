import pytest
from leetcode.stack.decode_string import decode_string


@pytest.mark.parametrize(
    "string, expected",
    [
        ("3[a]2[bc]", "aaabcbc"),  # basic repetition
        ("3[a2[c]]", "accaccacc"),  # nested repetition
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),  # with suffix
        ("1[a]", "a"),  # single letter
        ("2[a2[b3[c]]]", "abcccbcccabcccbccc"),  # multiple nested levels
        ("abc", "abc"),  # no brackets
        ("10[a]", "aaaaaaaaaa"),  # large repeat
        ("2[ab3[c]d]", "abcccdabcccd"),  # mixed letters inside
    ],
)
def test_decode_string(string: str, expected: str):
    assert decode_string(string) == expected
