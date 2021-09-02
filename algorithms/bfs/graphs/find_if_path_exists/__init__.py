from typing import List


def valid_path(n: int, edges: List[List[int]], start: int, end: int) -> bool:
    """
    Finds a valid path in a graph from start to end and returns true if a valid path can be found, else returns false.

    Will use a BFS as we can be able to traverse the vertices 1 level at a time until we find if there is a valid path
    from start to end.

    @param n: Number of vertices in graph
    @param edges: List of edge pairs between nodes/vertices in a graph
    @param start: Start Vertex
    @param end: End Vertex
    @return: True if there is a valid path from start to end, false otherwise
    """
    if not edges:
        return True

    if [start, end] in edges or [end, start] in edges or n == 1:
        return True

    graph = [[] for _ in range(n)]
    queue = []

    for node_1, node_2 in edges:
        graph[node_1].append(node_2)
        graph[node_2].append(node_1)

    queue.append(start)
    visited = set()

    while queue:
        current_node = queue.pop(0)

        for neighbour in graph[current_node]:
            if neighbour in visited:
                continue
            visited.add(neighbour)
            if neighbour == end:
                return True

            for x in graph[neighbour]:
                queue.append(x)

    return False
