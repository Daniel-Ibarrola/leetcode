def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    """
    There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
    The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches
    the island's right and bottom edges.

    The island is partitioned into a grid of square cells. You are given an m x n integer matrix
    heights where heights[r][c] represents the height above sea level of the cell at (r, c).

    The island receives a lot of rain, and the rain water can flow to neighboring cells directly
    north, south, east, and west if the neighboring cell's height is less than or equal to the
    current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

    Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain
    water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

    Example 1:
        Input: heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4]
        ]
        Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

    Example 2:
        Input: heights = [[1]]
        Output: [[0,0]]

    Constraints:
        - m == heights.length
        - n == heights[i].length
        - 1 <= m, n <= 200
        - 0 <= heights[i][j] <= 10^5
    """
    rows = len(heights)
    columns = len(heights[0])

    pacific: set[tuple[int, int]] = set()
    atlantic: set[tuple[int, int]] = set()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def dfs(row: int, col: int, visited: set[tuple[int, int]]):
        if (row, col) in visited:
            return

        visited.add((row, col))
        for dr, dc in directions:
            next_row = row + dr
            next_col = col + dc

            if (
                0 <= next_row < rows
                and 0 <= next_col < columns
                and heights[next_row][next_col] >= heights[row][col]
            ):
                dfs(next_row, next_col, visited)

    for c in range(0, columns):
        dfs(0, c, pacific)

    for r in range(0, rows):
        dfs(r, 0, pacific)

    for c in range(0, columns):
        dfs(rows - 1, c, atlantic)

    for r in range(0, rows):
        dfs(r, columns - 1, atlantic)

    all_cells = atlantic.intersection(pacific)
    return [[r, c] for r, c in all_cells]
