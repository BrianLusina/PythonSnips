from typing import List, Dict, Optional
from collections import deque


def reconstruct_path(previous_nodes, start_node, end_node):
    reversed_shortest_path = []

    # Start from the end of the path and work backwards
    current_node = end_node
    while current_node:
        reversed_shortest_path.append(current_node)
        current_node = previous_nodes[current_node]

    # Reverse our path to get the right order
    reversed_shortest_path.reverse()  # flip it around, in place
    return reversed_shortest_path  # no longer reversed


def mesh_message(graph: Dict, start_node: str, end_node: str) -> Optional[List]:
    if start_node not in graph:
        raise Exception("start node node in graph")
    if end_node not in graph:
        raise Exception("end node node in graph")

    nodes_to_visit = deque()
    nodes_to_visit.append(start_node)

    # Keep track of how we got to each node
    # We'll use this to reconstruct the shortest path at the end
    # We'll ALSO use this to keep track of which nodes we've
    # already visited
    how_we_reached_nodes = {start_node: None}

    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.popleft()

        # stop when we reach the end node
        if current_node == end_node:
            return reconstruct_path(how_we_reached_nodes, start_node, end_node)

        for neighbour in graph[current_node]:
            if neighbour not in how_we_reached_nodes:
                nodes_to_visit.append(neighbour)
                how_we_reached_nodes[neighbour] = current_node

    # If we get here, then we never found the end node
    # so there's NO path from start_node to end_node
    return None
