import pytest

from leetcode.greedy.min_refuel_stops import min_refuel_stops


@pytest.mark.parametrize(
    "target, start_fuel, stations, expected",
    [
        # Example 1: No need to refuel
        (1, 1, [], 0),
        # Example 2: Can't even reach first station
        (100, 1, [[10, 100]], -1),
        # Example 3: Multiple stops needed
        (100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]], 2),
        # Case: Exactly enough fuel without any station
        (50, 50, [], 0),
        # Large jump needed
        (100, 1, [[1, 99]], 1),
        # Can reach exactly with a single large refill
        (100, 50, [[25, 50], [50, 25]], 1),
        # All stations too far
        (100, 50, [[60, 10], [70, 20]], -1),
        # Edge: station right at the end
        (100, 50, [[100, 50]], -1),
        # Case: Station at 0 miles
        (100, 1, [[0, 100]], 1),
        # Station at destination (still allowed)
        (100, 50, [[100, 50]], -1),
        (100, 10, [[10, 60], [20, 10], [30, 10], [60, 10]], 4),
        (999, 1000, [[5, 100], [997, 100], [998, 100]], 0),
        (100, 25, [[25, 25], [50, 25], [75, 25]], 3),
    ],
)
def test_min_refuel_stops(
    target: int, start_fuel: int, stations: list[list[int]], expected: int
):
    assert min_refuel_stops(target, start_fuel, stations) == expected
