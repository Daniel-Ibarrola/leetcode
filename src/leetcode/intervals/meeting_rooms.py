def can_attend_meetings(intervals: list[tuple[int, int]]) -> bool:
    if not intervals:
        return True

    # sort by start time
    intervals.sort(key=lambda x: x[0])
    previous_meeting = intervals[0]

    for ii in range(1, len(intervals)):
        current_meeting = intervals[ii]

        previous_meeting_end = previous_meeting[1]
        current_meeting_start = current_meeting[0]

        if previous_meeting_end > current_meeting_start:
            return False

        previous_meeting = current_meeting

    return True
