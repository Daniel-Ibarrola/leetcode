def is_before(this_interval: tuple[int, int], other_interval: tuple[int, int]) -> bool:
    """Checks if other_interval is before this_interval."""
    this_start, this_end = this_interval
    other_start, other_end = other_interval
    return other_end < this_start


def insert_interval(intervals: list[tuple[int, int]], new_interval: tuple[int, int]):
    updated_intervals: list[tuple[int, int]] = []
    ii = 0

    while ii < len(intervals) and is_before(new_interval, intervals[ii]):
        updated_intervals.append(intervals[ii])
        ii += 1

    merged_start, merged_end = new_interval
    while ii < len(intervals) and intervals[ii][0] <= new_interval[1]:
        merged_start = min(merged_start, intervals[ii][0])
        merged_end = max(merged_end, intervals[ii][1])
        ii += 1

    updated_intervals.append((merged_start, merged_end))

    for jj in range(ii, len(intervals)):
        updated_intervals.append(intervals[jj])

    return updated_intervals
