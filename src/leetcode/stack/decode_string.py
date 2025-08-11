def decode_string(string: str) -> str:
    stack = []
    current_string = ""
    current_number = 0

    for char in string:
        if char.isdigit():
            # Multiply by 10 because we can have numbers with more than one digit
            current_number = current_number * 10 + int(char)
        elif char == "[":
            stack.append((current_string, current_number))
            current_string = ""
            current_number = 0
        elif char == "]":
            sub_string, repetitions = stack.pop()
            current_string = sub_string + current_string * repetitions
        else:
            current_string += char

    return current_string
