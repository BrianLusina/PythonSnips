from typing import List, DefaultDict, Set
from collections import defaultdict


def valid_tree(n: int, edges: List[List[int]]) -> bool:
    if len(edges) > (n - 1):
        return False

    graph: DefaultDict[int, List[int]] = defaultdict(list)
    for edge in edges:
        x, y = edge
        graph[x].append(y)
        graph[y].append(x)

    visited: Set[int] = set()

    def dfs(node: int, parent: int) -> bool:
        if node in visited:
            return False
        visited.add(node)

        neighbors = graph[node]
        for neighbor in neighbors:
            if neighbor == parent:
                continue
            if not dfs(neighbor, node):
                return False
        return True

    return dfs(0, -1) and len(visited) == n
