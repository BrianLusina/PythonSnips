from typing import List


def is_self_crossing(distance: List[int]) -> bool:
    # If there are fewer than four moves, crossing is impossible
    if len(distance) < 4:
        return False

    # Iterate through the distance list starting from index 3
    for i in range(3, len(distance)):
        # Case 1: Fourth line crosses the first line
        # This happens when the current distance is greater than or equal to the distance two steps back,
        # and the previous step is less than or equal to the step three steps back.
        if distance[i] >= distance[i - 2] and distance[i - 3] >= distance[i - 1]:
            return True

        # Case 2: Fifth line meets the first line (overlap)
        # This occurs when the previous step equals the step three steps back,
        # and the sum of the current step and the step four steps back is greater than or equal to the step two steps back.
        if (
            i >= 4
            and distance[i - 1] == distance[i - 3]
            and distance[i] >= distance[i - 2] - distance[i - 4]
        ):
            return True

        # Case 3: Sixth line crosses the first line (spiral crossing)
        # This happens when:
        # - The fourth step is greater than or equal to the second step.
        # - The sum of the current step and the fourth step is greater than or equal to the second step.
        # - The fifth step is less than or equal to the third step.
        # - The sum of the fifth step and the first step is greater than or equal to the third step.
        if (
            i >= 5
            and distance[i - 4] <= distance[i - 2] <= distance[i] + distance[i - 4]
            and distance[i - 1] <= distance[i - 3] <= distance[i - 1] + distance[i - 5]
        ):
            return True

    # If no crossing is detected, return False
    return False
