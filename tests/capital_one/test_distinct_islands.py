from leetcode.capital_one.distinct_islands import count_distinct_islands


class TestDistinctIslands:

    def test_two_identical_islands(self):
        grid = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1],
        ]
        assert count_distinct_islands(grid) == 1

    def test_three_distinct_islands(self):
        grid = [
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
        ]
        assert count_distinct_islands(grid) == 3

    def test_no_islands(self):
        grid = [
            [0, 0, 0],
            [0, 0, 0],
        ]
        assert count_distinct_islands(grid) == 0

    def test_single_cell_islands(self):
        grid = [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1],
        ]
        assert count_distinct_islands(grid) == 1

    def test_l_shaped_and_straight(self):
        grid = [
            [1, 1, 0, 1],
            [1, 0, 0, 1],
            [0, 0, 0, 1],
        ]
        assert count_distinct_islands(grid) == 2
