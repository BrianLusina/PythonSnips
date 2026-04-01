from typing import List, DefaultDict
from collections import deque, defaultdict


def sort_items(
    n: int, m: int, group: List[int], before_items: List[List[int]]
) -> List[int]:
    # Assign new group IDs to ungrouped items. -1 means ungrouped
    for i in range(n):
        if group[i] == -1:
            group[i] = m
            m += 1

    # Initialize adjacency lists for item level and group level graphs
    item_graph: DefaultDict[int, List[int]] = defaultdict(list)
    group_graph: DefaultDict[int, List[int]] = defaultdict(list)

    # Lists to store in-degree graphs for items and groups
    item_indegree: List[int] = [0] * n
    group_indegree: List[int] = [0] * m

    # Build dependency graphs
    for current in range(n):
        for previous in before_items[current]:
            # Add item-level edge
            item_graph[previous].append(current)
            item_indegree[current] += 1

            # Add group-level edge
            if group[previous] != group[current]:
                group_graph[group[previous]].append(group[current])
                group_indegree[group[current]] += 1

    def topological_sort(
        total_nodes: int, graph: DefaultDict[int, List[int]], in_degree: List[int]
    ) -> List[int]:
        queue = deque()

        # Add all nodes with 0 in-degree to the queue
        for node in range(total_nodes):
            if in_degree[node] == 0:
                queue.append(node)

        order = []

        # Process in topological order
        while queue:
            node = queue.popleft()
            order.append(node)

            # Reduce in-degree of all neighbours
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If all nodes are processed, return valid order, otherwise return empty list(cycle detected)
        return order if len(order) == total_nodes else []

    # Topologically sort items and groups
    item_order = topological_sort(n, item_graph, item_indegree)
    group_order = topological_sort(m, group_graph, group_indegree)

    # If either order is empty, a cycle exists, meaning no valid ordering
    if len(item_order) == 0 or len(group_order) == 0:
        return []

    # Group items based on their group IDs
    group_to_items: DefaultDict[int, List[int]] = defaultdict(list)
    for item in item_order:
        group_to_items[group[item]].append(item)

    # Build a final sort order following the group order
    result = []
    for g in group_order:
        result.extend(group_to_items[g])

    return result
