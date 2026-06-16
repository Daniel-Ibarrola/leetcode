from leetcode.graphs.number_of_islands import num_islands


def test_single_island():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert num_islands(grid) == 1


def test_multiple_islands():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert num_islands(grid) == 3


def test_no_islands():
    grid = [
        ["0", "0", "0"],
        ["0", "0", "0"],
    ]
    assert num_islands(grid) == 0


def test_all_land():
    grid = [
        ["1", "1"],
        ["1", "1"],
    ]
    assert num_islands(grid) == 1


def test_single_cell_land():
    assert num_islands([["1"]]) == 1


def test_single_cell_water():
    assert num_islands([["0"]]) == 0


def test_islands_diagonal_not_connected():
    # Diagonal adjacency does not count — these are 4 separate islands
    grid = [
        ["1", "0", "1"],
        ["0", "1", "0"],
        ["1", "0", "1"],
    ]
    assert num_islands(grid) == 5


def test_single_row():
    grid = [["1", "0", "1", "1", "0", "1"]]
    assert num_islands(grid) == 3


def test_single_column():
    grid = [["1"], ["0"], ["1"], ["1"]]
    assert num_islands(grid) == 2
