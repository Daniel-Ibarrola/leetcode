def has_valid_parentheses(string: str) -> bool:
    open_parentheses_types = {"(", "{", "["}
    close_parentheses_types = {")", "}", "]"}

    parentheses_map = {"(": ")", "{": "}", "[": "]"}

    stack = []

    for char in string:
        if char in open_parentheses_types:
            stack.append(char)
        elif char in close_parentheses_types:
            if len(stack) == 0:
                return False

            open_parentheses = stack.pop()
            if parentheses_map[open_parentheses] != char:
                return False

    return len(stack) == 0
