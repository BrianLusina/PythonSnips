from collections import defaultdict
from queue import Queue
from typing import List


def find_shortest(graph_nodes: int, graph_from: List[int], graph_to: List[int], ids: List[int], val: int) -> int:
    """
    Finds the length of the shortest path to node of color val
    @param graph_nodes: Number of nodes in the graph
    @type graph_nodes int
    @param graph_from: list of vertices/nodes sources
    @type graph_from list
    @param graph_to: List of vertices/nodes destinations
    @type graph_to list
    @param ids: List of ids representing the color of the nodes in order
    @type ids list
    @param val: the color to evaluate
    @type val int
    @return: shortest path length to node of color val
    @rtype int
    """
    graph = defaultdict(set)

    for source, destination in zip(graph_from, graph_to):
        graph[source].add(destination)
        graph[destination].add(source)

    color_to_match = ids[val - 1]

    visited = set()
    queue = Queue()
    queue.put([val, 0])
    visited.add(val)

    while not queue.empty():
        source, distance = queue.get()

        for neighbour in graph[source]:
            if neighbour not in visited:
                if ids[neighbour - 1] == color_to_match:
                    return distance + 1

                queue.put([neighbour, distance + 1])
                visited.add(neighbour)
    return -1
