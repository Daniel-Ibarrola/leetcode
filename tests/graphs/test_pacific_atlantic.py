from leetcode.graphs.pacific_atlantic import pacific_atlantic


def test_example_one():
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    result = sorted(map(tuple, pacific_atlantic(heights)))
    expected = sorted([(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)])
    assert result == expected


def test_single_cell():
    assert pacific_atlantic([[1]]) == [[0, 0]]


def test_single_row():
    # Every cell in a single row borders both oceans
    heights = [[1, 2, 3]]
    result = sorted(map(tuple, pacific_atlantic(heights)))
    expected = sorted([(0, 0), (0, 1), (0, 2)])
    assert result == expected


def test_single_column():
    heights = [[1], [2], [3]]
    result = sorted(map(tuple, pacific_atlantic(heights)))
    expected = sorted([(0, 0), (1, 0), (2, 0)])
    assert result == expected


def test_flat_grid():
    # All cells have equal height so water flows freely everywhere
    heights = [
        [1, 1],
        [1, 1],
    ]
    result = sorted(map(tuple, pacific_atlantic(heights)))
    expected = sorted([(0, 0), (0, 1), (1, 0), (1, 1)])
    assert result == expected


def test_decreasing_heights():
    # Water flows from high to low; only top-left corner can reach Pacific,
    # only bottom-right corner can reach Atlantic, but the peak must reach both
    heights = [
        [3, 2, 1],
        [2, 1, 0],
        [1, 0, 0],
    ]
    result = sorted(map(tuple, pacific_atlantic(heights)))
    # Top row and left column border Pacific; bottom row and right column border Atlantic
    # Cell (0,0) reaches Pacific (it IS on Pacific border) and can it reach Atlantic?
    # From (0,0)=3, water flows right and down, eventually reaching Atlantic borders
    assert (0, 0) in result


def test_peak_in_center():
    heights = [
        [1, 1, 1],
        [1, 9, 1],
        [1, 1, 1],
    ]
    result = sorted(map(tuple, pacific_atlantic(heights)))
    # Center peak (1,1)=9 is higher than all neighbors, water from it can flow to all borders
    assert (1, 1) in result
