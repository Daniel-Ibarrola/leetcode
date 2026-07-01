def longest_increasing_path(matrix: list[list[int]]) -> int:
    """
    Given an m x n integer matrix, return the length of the longest increasing path.

    From each cell, you can move in four directions: left, right, up, or down.
    You may not move diagonally or outside the boundary.
    You may not move to a cell with an equal or smaller value.

    Example 1:
        Input: matrix = [[9, 9, 4],
                         [6, 6, 8],
                         [2, 1, 1]]
        Output: 4
        Explanation: The longest increasing path is [1, 2, 6, 9].

    Example 2:
        Input: matrix = [[3, 4, 5],
                         [3, 2, 6],
                         [2, 2, 1]]
        Output: 4
        Explanation: The longest increasing path is [3, 4, 5, 6].

    Example 3:
        Input: matrix = [[1]]
        Output: 1

    Constraints:
        - m == matrix.length
        - n == matrix[i].length
        - 1 <= m, n <= 200
        - 0 <= matrix[i][j] <= 2^31 - 1
    """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    rows = len(matrix)
    cols = len(matrix[0])

    def is_valid_row(r: int) -> bool:
        return 0 <= r < rows

    def is_valid_col(c: int) -> bool:
        return 0 <= c < cols

    longest_found: dict[tuple[int, int], int] = {}

    def dfs(row: int, col: int) -> int:
        if (row, col) in longest_found:
            return longest_found[(row, col)]

        max_from_neighbors = 0
        for dr, dc in directions:
            next_row = row + dr
            next_col = col + dc

            if (
                is_valid_row(next_row)
                and is_valid_col(next_col)
                and matrix[next_row][next_col] > matrix[row][col]
            ):
                max_from_neighbors = max(
                    dfs(next_row, next_col) + 1, max_from_neighbors
                )

        longest_found[(row, col)] = max_from_neighbors
        return max_from_neighbors

    max_len = 0
    for r in range(rows):
        for c in range(cols):
            max_len = max(dfs(r, c), max_len)

    return max_len + 1
