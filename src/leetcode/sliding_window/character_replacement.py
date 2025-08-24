def _can_form_string_with_same_letters(
    char_count: dict[str, int], replacement_times: int
):
    max_count_char = max(char_count, key=char_count.get)
    total_count = 0
    for char, count in char_count.items():
        if char != max_count_char:
            total_count += count

    return total_count <= replacement_times


def character_replacement(string: str, replacement_times: int):
    start = 0
    max_length = 0
    char_count: dict[str, int] = {}

    for end in range(len(string)):
        char_count[string[end]] = char_count.get(string[end], 0) + 1

        while not _can_form_string_with_same_letters(char_count, replacement_times):
            char_count[string[start]] -= 1
            if char_count[string[start]] == 0:
                del char_count[string[start]]
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length
