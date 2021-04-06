def minimum_swaps(arr: list) -> int:
    """
    Time Complexity: O(n Log n) 
    Auxiliary Space: O(n)
    """
    length = len(arr)

    # Create list of pairs where each pair; the first element in the pair is the index of the element & second is
    # the value
    array_positions = [*enumerate(arr)]

    # Sort the array by values to get the right position of every element
    array_positions.sort(key=lambda x: x[1])

    # keep track of visited elements. Initialize all emements as not visited(False)
    visited_map = {k: False for k in range(length)}

    # keep track of swaps so far
    swaps = 0

    for x in range(length):

        # if we have already visited the element or at the correct position
        if visited_map[x] or array_positions[x][0] == x:
            continue

        # find number of nodes in this cycle
        cycles = 0
        y = x

        while not visited_map[y]:
            # mark node as visited
            visited_map[y] = True

            # move to next node
            y = array_positions[y][0]
            cycles += 1

        # update by adding current cycle - 1
        if cycles > 0:
            swaps += (cycles - 1)

    return swaps
