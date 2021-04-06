def time_frog_jumps(other_side_position: int, leaf_positions: list) -> int:
    """
    Returns the earliest time that a frog can jump to the other side of the river.

    Uses a Set to store unique values from leaf_positions[]. 
    When the size equals to other_side_position, means the leaves have covered all positions from 1 to other_side_position. 
    So the frog can get to the position other_side_position + 1.
    :param other_side_position
    :param leaf_positions
    :returns earliest time that a frog can jump to the other side of the river
    :rtype int
    """
    s = set()

    for time in range(len(leaf_positions)):
        s.add(leaf_positions[time])

        if len(s) == other_side_position:
            return time

    return -1
