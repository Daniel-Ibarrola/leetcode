def find_content_children(greed_factor: list[int], size: list[int]) -> int:
    """
    You are given two integer arrays:

    greed_factor (of size n), where each element represents the minimum size of a cookie that a child needs to be satisfied.

    size (of size m), where each element represents the size of a cookie.

    Your task is to assign cookies to children such that as many children as possible are satisfied.
    A child is satisfied if the cookie they receive is equal to or greater than their greed factor.
    Each child can receive at most one cookie, and each cookie can be given to only one child.
    Write a function to return the maximum number of children that can be satisfied.

    """
    greed_factor.sort()
    size.sort()

    size_index = 0
    greed_index = 0
    max_children = 0

    while size_index < len(size) and greed_index < len(greed_factor):
        if size[size_index] >= greed_factor[greed_index]:
            max_children += 1
            greed_index += 1
        size_index += 1

    return max_children
