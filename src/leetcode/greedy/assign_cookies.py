def find_content_children(greed_factor: list[int], size: list[int]) -> int:
    greed_factor.sort()
    size.sort()

    greed_index, size_index = 0, 0
    content_children = 0

    while greed_index < len(greed_factor) and size_index < len(size):
        if greed_factor[greed_index] <= size[size_index]:
            content_children += 1
            greed_index += 1
        size_index += 1

    return content_children
