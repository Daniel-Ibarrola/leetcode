import heapq


def min_refuel_stops(target: int, start_fuel: int, stations: list[list[int]]) -> int:
    if start_fuel >= target:
        return 0

    # Sort stations by position (important for reachable check)
    stations.sort(key=lambda x: x[0])

    # Max heap of available fuels (store as negative for heapq)
    max_heap: list[int] = []
    stops = 0
    current_fuel = start_fuel
    station_idx = 0

    while current_fuel < target:
        # Add all reachable stations to the heap
        while station_idx < len(stations) and stations[station_idx][0] <= current_fuel:
            heapq.heappush(max_heap, -stations[station_idx][1])
            station_idx += 1

        # If no reachable stations and we haven't reached the target, fail
        if not max_heap:
            return -1

        # Refuel at the station with the most fuel we've passed
        current_fuel += -heapq.heappop(max_heap)
        stops += 1

    return stops
