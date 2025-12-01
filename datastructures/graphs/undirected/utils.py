from typing import List, DefaultDict, Dict, Optional
from collections import defaultdict, deque


def closest_node(n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
    # build and adjacency list
    adj_list: DefaultDict[int, List[int]] = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    def bfs_distance(start: int) -> List[int]:
        """
        Compute the shortest distance from start node to all other nodes using BFS.
        Returns a list where distances[i] is the distance from start to node i.
        """
        # -1 means not visited
        distances = [-1] * n
        distances[start] = 0
        queue = deque([start])

        while queue:
            node = queue.popleft()
            for neighbor in adj_list[node]:
                if distances[neighbor] == -1:  # Not visited
                    distances[neighbor] = distances[node] + 1
                    queue.append(neighbor)

        return distances

    def find_path(start: int, end: int) -> List[int]:
        """
        Find the unique path from start to end in the tree using BFS.
        Returns the list of nodes on the path (including start and end).
        """
        if start == end:
            return [start]

        # BFS to find path, keeping track of parent pointers
        parent: Dict[int, Optional[int]] = {start: None}
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node == end:
                break

            for neighbor in adj_list[node]:
                # not visited
                if neighbor not in parent:
                    parent[neighbor] = node
                    queue.append(neighbor)

        # Reconstruct path from end to start using pointers
        path = []
        current = end
        # Add safety check: limit iterations to avoid infinite loops
        # In a tree with n nodes, path length can't exceed n
        for _ in range(n):
            if current not in parent:
                # This shouldn't happen in a valid connected tree
                break
            path.append(current)
            if current == start:
                # We've reached the start, we're done
                break
            current = parent[current]

        # reverse to get the path start to end
        return path[::-1]

    result = []
    for start, end, target in query:
        # find the path from start to end
        found_path = find_path(start, end)

        # compute distances from target node to all nodes
        distances_from_target = bfs_distance(target)

        # Find the node on the path with minimum distance to target
        # If there's a tie, we want the one with the smallest index
        min_distance = float("inf")
        closest = -1

        for node in found_path:
            dist = distances_from_target[node]
            # Update if we found a closer node, or same distance but smaller index
            if dist < min_distance or (dist == min_distance and node < closest):
                min_distance = dist
                closest = node

        result.append(closest)

    return result
