import pytest

from leetcode.intervals.merge_intervals import Interval, merge_intervals


@pytest.mark.parametrize(
    "intervals, expected",
    [
        # ✅ Example case
        (
            [
                Interval(3, 5),
                Interval(1, 4),
                Interval(7, 9),
                Interval(6, 8),
            ],
            [Interval(1, 5), Interval(6, 9)],
        ),
        # ✅ Already sorted with overlap
        (
            [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)],
            [Interval(1, 6), Interval(8, 10), Interval(15, 18)],
        ),
        # ✅ Touching intervals should merge
        ([Interval(1, 4), Interval(4, 5)], [Interval(1, 5)]),
        ([Interval(1, 2), Interval(2, 3), Interval(3, 4)], [Interval(1, 4)]),
        # ✅ Unsorted input
        (
            [Interval(8, 10), Interval(1, 3), Interval(2, 6), Interval(15, 18)],
            [Interval(1, 6), Interval(8, 10), Interval(15, 18)],
        ),
        # ✅ One interval fully contains others
        (
            [Interval(1, 10), Interval(2, 3), Interval(4, 8), Interval(9, 10)],
            [Interval(1, 10)],
        ),
        # ✅ Duplicate intervals
        ([Interval(1, 4), Interval(1, 4), Interval(1, 4)], [Interval(1, 4)]),
        # ✅ No overlap
        (
            [Interval(1, 2), Interval(4, 5), Interval(7, 8)],
            [Interval(1, 2), Interval(4, 5), Interval(7, 8)],
        ),
        # ✅ Single interval
        ([Interval(1, 5)], [Interval(1, 5)]),
        # ✅ Empty input
        ([], []),
        # ✅ Zero-length intervals
        (
            [Interval(1, 1), Interval(1, 2), Interval(3, 3)],
            [Interval(1, 2), Interval(3, 3)],
        ),
        # ✅ Negative numbers
        (
            [Interval(-10, -1), Interval(-5, 0), Interval(1, 3)],
            [Interval(-10, 0), Interval(1, 3)],
        ),
    ],
)
def test_merge_intervals(intervals, expected):
    assert merge_intervals(intervals) == expected
