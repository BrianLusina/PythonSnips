from typing import List, Deque, Set, Tuple
from collections import deque


def shortest_path_length(graph: List[List[int]]) -> int:
    """
    Returns the shortest path length from one vertex in the graph to another while visiting all vertices.
    Args:
        graph (List[List[int]]): a 2D list of integers representing the vertices in the graph as an adjacency list.
    Returns:
        int: the shortest path length
    """

    n = len(graph)
    # A graph with 1 or 0 nodes is already "fully visited" in 0 steps
    if n <= 1:
        return 0
    # The target bitmask has all n bits set to 1
    # Example for n=3: (1 << 3) - 1 = 0b111
    target_mask = (1 << n) - 1

    # Queue stores: (current_node, visited_mask, distance)
    # We start a BFS from every node simultaneously to find the global minimum
    queue: Deque[Tuple[int, int, int]] = deque([(i, 1 << i, 0) for i in range(n)])

    # Visited set stores: (current_node, visited_mask)
    # This prevents us from re-processing the same state at a longer distance
    visited: Set[Tuple[int, int]] = {(i, 1 << i) for i in range(n)}

    while queue:
        current_node, mask, distance = queue.popleft()

        # If the current mask matches our target, we've visited every node
        if mask == target_mask:
            return distance

        # Explore neighbors
        for neighbor in graph[current_node]:
            # For each neighbour, we create a new mask
            new_mask = mask | (1 << neighbor)
            if (neighbor, new_mask) not in visited:
                visited.add((neighbor, new_mask))
                queue.append((neighbor, new_mask, distance + 1))

    return -1
