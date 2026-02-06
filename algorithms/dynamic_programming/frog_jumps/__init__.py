def frog_jumps(x: int, y: int, d: int) -> int:
    jumps = 0

    # no need to jump, we are already there
    if y == x:
        return jumps

    distance_to_cover = y - x

    # it will only take us 1 jump
    if distance_to_cover < d:
        return 1

    if distance_to_cover % d == 0:
        jumps = distance_to_cover // d

    else:
        jumps = (distance_to_cover // d) + 1

    return jumps
