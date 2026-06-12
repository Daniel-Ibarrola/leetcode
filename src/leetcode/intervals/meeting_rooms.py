def can_attend_meetings(intervals: list[tuple[int, int]]) -> bool:
    """
    Checks if a person can attend all the meetings scheduled without any time conflicts.

    Given an array intervals, where each element [s1, e1] represents a meeting starting at time s1 and ending at time e1,
    determines if there are any overlapping meetings.

    If there is no overlap between any meetings, returns true; otherwise, returns false.
    Note that meetings ending and starting at the same time, such as (0,5) and (5,10), do not conflict.

    """
    intervals.sort(key=lambda x: x[0])

    for i in range(len(intervals) - 1):
        prev_meeting = intervals[i]
        current_meeting = intervals[i + 1]

        if prev_meeting[1] > current_meeting[0]:
            return False

    return True
