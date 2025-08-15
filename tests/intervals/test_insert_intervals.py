from leetcode.intervals.insert_interval import (
    is_before,
    insert_interval,
)
import pytest


class TestInsertInterval:

    def test_is_before(self):
        interval = (6, 9)
        assert is_before(interval, (2, 4)) is True
        assert is_before(interval, (7, 8)) is False  # overlaps
        assert is_before(interval, (10, 15)) is False

    @pytest.mark.parametrize(
        "intervals, new_interval, expected",
        [
            # Example 1
            ([(1, 3), (6, 9)], (2, 5), [(1, 5), (6, 9)]),
            # Example 2
            (
                [(1, 2), (3, 5), (6, 7), (8, 10), (12, 16)],
                (4, 8),
                [(1, 2), (3, 10), (12, 16)],
            ),
            # No overlap, insert at beginning
            ([(5, 7), (8, 10)], (1, 2), [(1, 2), (5, 7), (8, 10)]),
            # No overlap, insert at end
            ([(1, 3), (5, 7)], (10, 12), [(1, 3), (5, 7), (10, 12)]),
            # Overlaps with all
            ([(1, 3), (4, 5), (6, 8)], (0, 10), [(0, 10)]),
            # Touching intervals (should merge)
            ([(1, 2), (5, 7)], (2, 5), [(1, 7)]),
            # New interval inside existing interval
            ([(1, 10)], (3, 5), [(1, 10)]),
            # Multiple merges in middle
            ([(1, 3), (6, 9), (12, 16)], (4, 13), [(1, 3), (4, 16)]),
            # Empty intervals list
            ([], (4, 8), [(4, 8)]),
            # Single element intervals
            ([(1, 1), (3, 3), (5, 5)], (2, 4), [(1, 1), (2, 4), (5, 5)]),
        ],
    )
    def test_insert_interval(
        self,
        intervals: list[tuple[int, int]],
        new_interval: tuple[int, int],
        expected: list[tuple[int, int]],
    ):
        assert insert_interval(intervals, new_interval) == expected
