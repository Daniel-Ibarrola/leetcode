def transform_array(arr: list[int]) -> list[int]:
    transformed: list[int] = []
    for ii in range(len(arr)):
        previous_element = arr[ii - 1] if ii - 1 >= 0 else 0
        next_element = arr[ii + 1] if ii + 1 < len(arr) else 0
        current = arr[ii]
        transformed.append(previous_element + current + next_element)

    return transformed
