from typing import List
from collections import defaultdict, deque


def frog_position(n: int, edges: List[List[int]], t: int, target: int) -> float:
    # Handle the trivial case of a single vertex
    if n == 1:
        return 1.0

    # Build adjacency list representation of the tree
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # BFS to track probabilities and arrival times
    # Each state: (vertex, parent, probability, time)
    queue = deque([(1, -1, 1.0, 0)])
    visited = {1}

    while queue:
        vertex, parent, prob, time = queue.popleft()

        # Find unvisited neighbors (excluding the parent we came from)
        unvisited_neighbors = [
            neighbor for neighbor in graph[vertex] if neighbor not in visited
        ]

        # Check if we're at the target vertex
        if vertex == target:
            # If we arrive exactly at time t, we're here
            if time == t:
                return prob
            # If we arrive before time t, we can only be here if this is a leaf
            # (no unvisited neighbors to continue to)
            elif time < t and len(unvisited_neighbors) == 0:
                return prob
            # Otherwise, we either haven't arrived yet or we moved past it
            else:
                return 0.0

        # If we've used up our time, stop exploring this path
        if time >= t:
            continue

        # Move to each unvisited neighbor with equal probability
        if unvisited_neighbors:
            # Probability splits equally among all unvisited neighbors
            next_prob = prob / len(unvisited_neighbors)

            for neighbor in unvisited_neighbors:
                visited.add(neighbor)
                queue.append((neighbor, vertex, next_prob, time + 1))

    # If we never reached the target, probability is 0
    return 0.0


def frog_position_2(n: int, edges: List[List[int]], t: int, target: int) -> float:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    q = deque([(1, 1.0)])
    visited = [False] * (n + 1)
    visited[1] = True

    time_left = t
    while q and time_left >= 0:
        level_size = len(q)

        for _ in range(level_size):
            u, p = q.popleft()

            cnt_unvisited = 0
            for v in graph[u]:
                if not visited[v]:
                    cnt_unvisited += 1

            if u == target:
                if time_left == 0 or cnt_unvisited == 0:
                    return p
                return 0.0

            if cnt_unvisited > 0:
                split = p / cnt_unvisited
                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append((v, split))
        time_left -= 1
    return 0.0
