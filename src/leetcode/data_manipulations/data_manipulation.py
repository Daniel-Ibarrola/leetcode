def check_for_pattern(pattern: str, source: str) -> int:
    vowels = {"a", "e", "i", "o", "u", "y"}
    pattern_len = len(pattern)

    count = 0
    for ii in range(len(source) - pattern_len + 1):
        match = True
        for jj in range(pattern_len):
            pattern_char = pattern[jj]
            source_char = source[ii + jj]

            if pattern_char == "0" and source_char not in vowels:
                match = False
                break
            elif pattern_char == "1" and source_char in vowels:
                match = False
                break

        if match:
            count += 1

    return count
