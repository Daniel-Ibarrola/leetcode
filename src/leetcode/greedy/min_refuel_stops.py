from typing import Optional


def min_refuel_stops(target: int, start_fuel: int, stations: list[list[int]]) -> int:
    if start_fuel >= target:
        return 0

    stops = 0

    current_fuel = start_fuel
    current_position = 0
    visited_stations: set[tuple[int, int]] = set()
    distance_to_target = target

    while distance_to_target > 0:
        #  Pick station with max fuel that can be reached
        max_reachable_station: Optional[tuple[int, int]] = None
        for station in stations:
            [position, fuel] = station
            if (position, fuel) not in visited_stations:
                if current_fuel >= position - current_position and (
                    max_reachable_station is None or fuel > max_reachable_station[1]
                ):
                    max_reachable_station = (position, fuel)

        if max_reachable_station:
            visited_stations.add(max_reachable_station)
        else:
            break

        [position, fuel] = max_reachable_station
        current_fuel += fuel - (position - current_position)

        stops += 1
        distance_to_target = target - position
        current_position = position

        if current_fuel >= distance_to_target:
            break

    if current_fuel < distance_to_target:
        return -1
    return stops
