from collections import defaultdict
from typing import List

WHITE = 1
GRAY = 2
BLACK = 3


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    adjacency_list = defaultdict(list)

    for destination, source in prerequisites:
        adjacency_list[source].append(destination)
    topological_sorted_order = []
    is_possible = True

    color = {k: WHITE for k in range(num_courses)}

    def dfs(node):
        nonlocal is_possible

        if not is_possible:
            return

        color[node] = GRAY

        if node in adjacency_list:
            for neighbour in adjacency_list[node]:
                if color[neighbour] == WHITE:
                    dfs(neighbour)
                elif color[neighbour] == GRAY:
                    is_possible = False

        color[node] = BLACK
        topological_sorted_order.append(node)

    for vertex in range(num_courses):
        if color[vertex] == WHITE:
            dfs(vertex)

    return topological_sorted_order[::-1] if is_possible else []
