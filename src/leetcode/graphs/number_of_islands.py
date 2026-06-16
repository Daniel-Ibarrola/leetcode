def num_islands(grid: list[list[str]]) -> int:
    """
    Given an m x n 2D binary grid of '1's (land) and '0's (water),
    return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent
    land cells horizontally or vertically. You may assume all four edges
    of the grid are surrounded by water.

    Example 1:
        Input:
            grid = [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ]
        Output: 1

    Example 2:
        Input:
            grid = [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ]
        Output: 3

    Constraints:
        - m == grid.length
        - n == grid[i].length
        - 1 <= m, n <= 300
        - grid[i][j] is '0' or '1'
    """
    visited: set[tuple[int, int]] = set()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(row: int, col: int):
        if (row, col) in visited:
            return

        # check if the cell is out of bounds
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return

        if grid[row][col] == "0":
            return

        visited.add((row, col))
        for dr, dc in directions:
            dfs(row + dr, col + dc)
        return

    rows = len(grid)
    cols = len(grid[0])
    n_islands = 0

    for row_ in range(rows):
        for col_ in range(cols):
            if (row_, col_) not in visited and grid[row_][col_] == "1":
                dfs(row_, col_)
                n_islands += 1

    return n_islands
