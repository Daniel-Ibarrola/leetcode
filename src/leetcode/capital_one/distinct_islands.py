import enum


class Direction(enum.Enum):
    START = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

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
    n_rows = len(grid)
    n_cols = len(grid[0])

    path: list[str] = []
    visited: set[tuple[int, int]] = set()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    grid_to_dir = {
        (0, 0): Direction.START,
        (-1, 0): Direction.UP,
        (1, 0): Direction.DOWN,
        (0, -1): Direction.LEFT,
        (0, 1): Direction.RIGHT,
    }

    def dfs(row: int, col: int, dir_: Direction):
        if (row, col) in visited:
            return

        visited.add((row, col))

        path.append(str(dir_.value))

        for dr, dc in directions:
            next_row = row + dr
            next_col = col + dc
            next_dir = grid_to_dir[(dr, dc)]
            if (
                0 <= next_row < n_rows
                and 0 <= next_col < n_cols
                and grid[next_row][next_col] == 1
            ):
                dfs(next_row, next_col, next_dir)

        path.append(f"-{dir_.value}")

    unique_islands: set[str] = set()

    for r in range(n_rows):
        for c in range(n_cols):
            if (r, c) not in visited and grid[r][c] == 1:
                dfs(r, c, Direction.START)
                unique_islands.add("".join(path))

                path.clear()

    return len(unique_islands)
