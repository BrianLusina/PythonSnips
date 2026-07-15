from typing import List


def max_distance(position: List[int], m: int) -> int:
    if not position:
        return 0
    if m <= 1:
        return 0

    result = 0
    n = len(position)
    sorted_positions = sorted(position)

    # initial search space
    low = 1
    high = int(sorted_positions[-1] / (m - 1.0)) + 1

    def can_place_balls(x: int) -> bool:
        """Check if we can place 'm' balls at 'position' with each ball having at least 'x' gap."""

        # place first ball at the first positions
        prev_ball_position = sorted_positions[0]
        balls_placed = 1

        # Iterate on each position and place a ball there if we can place it
        for i in range(1, n):
            current_position = sorted_positions[i]
            # check if we can place the ball at the current position
            if current_position - prev_ball_position >= x:
                balls_placed += 1
                prev_ball_position = current_position
            # if all m balls are placed return true
            if balls_placed == m:
                return True

        return False

    while low <= high:
        mid = low + (high - low) // 2
        # if we can place all balls having a gap at least mid
        if can_place_balls(mid):
            # Then mid can be our answer
            result = mid
            # and discard the left-half search space
            low = mid + 1
        else:
            # discard the right-half search space
            high = mid - 1

    return result
