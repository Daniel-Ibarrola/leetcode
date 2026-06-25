def count_distinct_islands(grid: list[list[int]]) -> int:
    """Given a binary matrix where 1 represents land and 0 represents water,
    count the number of distinct islands.

    Two islands are considered distinct if and only if they have different shapes.
    An island's shape is defined by the relative positions of its cells — two islands
    are the same shape if one can be translated (but not rotated or reflected) to match the other.

    Example 1:
        Input:
            grid = [
                [1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1],
                [0, 0, 0, 1, 1],
            ]
        Output: 1
        Explanation: Both 2x2 blocks have the same shape.

    Example 2:
        Input:
            grid = [
                [1, 1, 0, 1, 1],
                [1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [1, 1, 0, 1, 0],
            ]
        Output: 3
        Explanation: The top-left, top-right, and bottom islands all have different shapes.

    Constraints:
        - 1 <= rows, cols <= 50
        - grid[i][j] is either 0 or 1

    :param grid: binary matrix representing a map of land and water
    :return: number of distinct island shapes
    """
    pass
