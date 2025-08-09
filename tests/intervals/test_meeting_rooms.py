import pytest
from leetcode.intervals.meeting_rooms import can_attend_meetings


@pytest.mark.parametrize(
    "intervals, expected",
    [
        # ✅ No overlap, can attend all
        ([(0, 30)], True),  # Only one meeting
        ([(0, 5), (5, 10)], True),  # Touching at the boundary
        ([(1, 2), (3, 4), (5, 6)], True),  # Completely separate meetings
        ([(0, 10), (15, 25), (30, 40)], True),  # Large gaps
        # ❌ Overlaps, cannot attend all
        ([(0, 30), (5, 10)], False),  # Second starts before first ends
        ([(7, 10), (2, 4), (3, 6)], False),  # Overlaps inside range
        ([(1, 5), (2, 6)], False),  # Full overlap
        ([(1, 10), (5, 8)], False),  # Nested meeting
        ([(5, 10), (10, 15), (14, 20)], False),  # Last one overlaps with previous
        # 🔹 Edge cases
        ([], True),  # No meetings at all
        ([(1, 1)], True),  # Zero-length meeting
        ([(1, 2), (2, 2)], True),  # Consecutive zero-length
        ([(1, 2), (2, 3), (3, 5)], True),  # Back-to-back with no overlap
    ],
)
def test_can_attend_meetings(intervals, expected):
    assert can_attend_meetings(intervals) == expected
