from typing import List
import heapq


def min_refuel_stops(target: int, start_fuel: int, stations: List[List[int]]):
    # if the start fuel is 0, we can't start the journey
    if start_fuel == 0:
        return -1

    # No need to stop to refuel, the car can reach the target distance with the starting fuel
    if start_fuel >= target:
        return 0

    # Create a max heap to store the fuel capacities of stations in
    # such a way that maximum fuel capacity is at the top of the heap
    max_heap = []
    i, n = 0, len(stations)
    # This will keep track of the minimum refueling stops
    min_stops = 0
    max_distance = start_fuel

    # loop until the car reaches the target, or it is out of fuel
    while max_distance < target:
        # If there are still stations and the next one is within range, add its fuel capacity to the max heap
        if i < n and stations[i][0] <= max_distance:
            heapq.heappush(max_heap, -stations[i][1])
            i += 1
        # If there are no more stations, and we can't reach the target, return -1
        elif not max_heap:
            return -1
        else:
            # Otherwise, fill up at the station with the highest fuel capacity and increment stops
            max_distance += -heapq.heappop(max_heap)
            min_stops += 1

    return min_stops


def min_refuel_stops_2(target: int, start_fuel: int, stations: List[List[int]]):
    # if the start fuel is 0, we can't start the journey
    if start_fuel == 0:
        return -1

    # No need to stop to refuel, the car can reach the target distance with the starting fuel
    if start_fuel >= target:
        return 0

    max_heap = []

    # Append target to stations to treat final destination as station with no fuel
    stations.append([target, 0])

    # This will keep track of the minimum refueling stops
    min_stops = 0
    # Keeps track of the distance covered from the start. This will be used to calculate the distance to the next station
    distance_covered = 0
    # Current fuel level is the current fuel level we have
    current_fuel_level = start_fuel

    for idx in range(len(stations)):
        station_distance, station_fuel = stations[idx]
        # The Fuel cost is the station distance from the beginning minus the distance covered so far
        fuel_cost = station_distance - distance_covered

        current_fuel_level -= fuel_cost

        while current_fuel_level < 0 and max_heap:
            current_fuel_level -= heapq.heappop(max_heap)
            min_stops += 1

        # check if we can reach the next station
        if current_fuel_level < 0:
            return -1

        heapq.heappush(max_heap, -station_fuel)
        distance_covered = station_distance

    return min_stops
