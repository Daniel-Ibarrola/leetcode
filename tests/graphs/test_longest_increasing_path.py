from leetcode.graphs.longest_increasing_path import longest_increasing_path


def test_single_cell():
    assert longest_increasing_path([[1]]) == 1


def test_single_row():
    # 1 → 2 → 3 → 4
    assert longest_increasing_path([[1, 2, 3, 4]]) == 4


def test_single_column():
    # 1 → 2 → 3
    assert longest_increasing_path([[1], [2], [3]]) == 3


def test_example_one():
    matrix = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1],
    ]
    assert longest_increasing_path(matrix) == 4


def test_example_two():
    matrix = [
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1],
    ]
    assert longest_increasing_path(matrix) == 4


def test_all_equal():
    # No moves possible — every cell has the same value
    matrix = [
        [5, 5],
        [5, 5],
    ]
    assert longest_increasing_path(matrix) == 1


def test_decreasing_row():
    # Can only traverse right-to-left: 1 ← 2 ← 3 ← 4
    assert longest_increasing_path([[4, 3, 2, 1]]) == 4


def test_diagonal_does_not_count():
    # Diagonal values are increasing but diagonal moves are not allowed
    matrix = [
        [1, 0],
        [0, 2],
    ]
    # Only valid paths: [1] or [2] from corners, length 1
    assert longest_increasing_path(matrix) == 2


def test_multiple_paths_same_length():
    # Two paths of equal max length
    matrix = [
        [1, 2],
        [4, 3],
    ]
    assert longest_increasing_path(matrix) == 4


def test_large_values():
    matrix = [
        [0, 2**31 - 1],
    ]
    assert longest_increasing_path(matrix) == 2
