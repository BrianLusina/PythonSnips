from typing import List, Tuple


def car_pooling(trips: List[List[int]], capacity: int) -> bool:
    """
    Calculates and checks whether it is possible to pick and drop of passengers on the given trips given the cars
    capacity
    Args:
        trips(list): The trips that the car makes while collecting passengers on the route
        capacity(int): capacity of the car
    Returns:
        bool: whether it is possible to collect and drop all passengers along the route
    """
    # For every trip, create two entries, the start with the passenger count and end with the passenger count
    events: List[Tuple[int, int]] = []

    # Create the events
    for trip in trips:
        num, start, end = trip
        # Mark the increase and decrease in passengers at pickup and drop-off points
        events.append((start, num))  # pick up
        events.append((end, -num))  # drop off

    # sort by the location
    # If locations are equal, the negative value (drop-off)
    # will naturally come before the positive value (pick-up)
    events.sort()

    # This keeps track of the current vehicle's capacity, which will be used along the trip to check how many passengers
    # have been carried so far
    current_occupancy = 0

    # process events chronologically
    for event in events:
        location, change = event
        current_occupancy += change
        if current_occupancy > capacity:
            return False

    return True


def car_pooling_bucket(trips: List[List[int]], capacity: int) -> bool:
    # Initialize a timeline to track changes in passenger count at each km mark (0 to 1000)
    timestamp = [0] * 1001

    # Mark the increase and decrease in passengers at pickup and drop-off points
    for trip in trips:
        num_passengers, start, end = trip
        timestamp[start] += num_passengers  # Pick up passengers
        timestamp[end] -= num_passengers  # Drop off passengers

    # Simulate the car's journey by applying the passenger changes
    used_capacity = 0
    for passenger_change in timestamp:
        used_capacity += passenger_change  # Update current passenger count
        if used_capacity > capacity:  # Check if capacity is exceeded
            return False  # Trip configuration is invalid

    return True  # All trips are valid within capacity
