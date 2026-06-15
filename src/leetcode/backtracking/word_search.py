def check_word_exists(board: list[list[str]], word: str) -> bool:
    """
    Given an m x n grid of characters board and a string word, return true if word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
    or vertically neighboring. The same letter cell may not be used more than once.

    """

    visited: set[tuple[int, int]] = set()

    def dfs(row: int, col: int, index: int) -> bool:
        if index == len(word):
            return True

        if (row, col) in visited:
            return False

        # check if the cell is out of bounds
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False

        if board[row][col] != word[index]:
            return False

        visited.add((row, col))

        return (
            dfs(row + 1, col, index + 1)
            or dfs(row - 1, col, index + 1)
            or dfs(row, col + 1, index + 1)
            or dfs(row, col - 1, index + 1)
        )

    rows, cols = len(board), len(board[0])
    # initialize depth-first search from
    # each of the cells that have the same first
    # letter as word
    for row_ in range(rows):
        for col_ in range(cols):
            if board[row_][col_] == word[0]:
                if dfs(row_, col_, 0):
                    return True
    return False
