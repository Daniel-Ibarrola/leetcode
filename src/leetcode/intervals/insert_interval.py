def insert_interval(
    intervals: list[tuple[int, int]], new_interval: tuple[int, int]
) -> list[tuple[int, int]]:
    """
    Given a list of intervals intervals and an interval newInterval, write a function to insert newInterval into
    a list of existing, non-overlapping, and sorted intervals based on their starting points.

    The function should ensure that after the new interval is added, the list remains sorted
    without any overlapping intervals, merging them if needed.


    Two intervals are considered overlapping if they share any common time,
    including if one ends exactly when another begins (e.g., [1,4] and [4,7] overlap and should be merged into [1,7]).
    """
    merged_intervals: list[tuple[int, int]] = []
    new_start, new_end = new_interval

    # Append all intervals that end before the new interval
    ii = 0
    while ii < len(intervals) and intervals[ii][1] < new_start:
        merged_intervals.append(intervals[ii])
        ii += 1

    # Construct merged intervals
    merged_start, merged_end = new_interval
    while ii < len(intervals) and new_end >= intervals[ii][0]:
        merged_start = min(intervals[ii][0], merged_start)
        merged_end = max(intervals[ii][1], merged_end)
        ii += 1

    merged_intervals.append((merged_start, merged_end))

    # Append all intervals after the new interval
    for jj in range(ii, len(intervals)):
        merged_intervals.append(intervals[jj])

    return merged_intervals
