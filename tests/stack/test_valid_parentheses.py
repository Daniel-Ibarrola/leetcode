import pytest
from leetcode.stack.valid_parantheses import has_valid_parentheses


@pytest.mark.parametrize(
    "string, expected",
    [
        # ✅ Basic valid cases
        ("()", True),
        ("()[]{}", True),
        ("([])", True),
        ("{[]}", True),
        ("[()]", True),
        ("((()))", True),  # Nested of the same type
        ("[({})]", True),  # Multiple nesting types
        # ❌ Invalid structure/order
        ("(]", False),  # Wrong closing type
        ("([)]", False),  # Wrong nesting order
        ("((", False),  # Missing closing
        ("))", False),  # Missing opening
        ("(()", False),  # Unbalanced opening
        ("())", False),  # Unbalanced closing
        ("[", False),  # Single open bracket
        ("]", False),  # Single close bracket
        # 🔹 Edge cases
        ("", True),  # Empty string is valid
        ("{}", True),  # Single pair of curly braces
        ("[{}]", True),  # One pair inside another
        ("(((((((((())))))))))", True),  # Deep nesting
        # ("((((((((()))))))))", False),  # Deep nesting but missing closing
        ("[({}[])]", True),  # Multiple valid patterns
    ],
)
def test_is_valid(string: str, expected: bool):
    assert has_valid_parentheses(string) == expected
