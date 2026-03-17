from typing import NamedTuple


class Interval(NamedTuple):
    start: int
    end: int


def merge_intervals(intervals: list[Interval]) -> list[Interval]:
    sorted_intervals = sorted(intervals, key=lambda i: i.start)

    merged_intervals: list[Interval] = []
    for interval in sorted_intervals:
        if not merged_intervals or merged_intervals[-1].end < interval.start:
            merged_intervals.append(interval)
        else:
            merged_intervals[-1] = Interval(
                start=merged_intervals[-1].start,
                end=max(merged_intervals[-1].end, interval.end),
            )

    return merged_intervals
