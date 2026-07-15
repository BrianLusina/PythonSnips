from typing import List, Dict, Tuple, Set, DefaultDict
from collections import defaultdict
from queue import PriorityQueue
import heapq


def network_delay_time(connections: List[List[int]], n: int, k: int) -> int:
    # If there is no list of times, then we return -1
    if not connections:
        return -1

    # Graph variable will contain the vertices as key value pairs, where the key is the source vertex, the value is the
    # destinations from the source vertex to other destinations. The value is a list as one can move from a vertex to
    # other vertices The list is a tuple, where the first value is the destination and the second value is the weight
    graph: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)
    # Vertices contain a set of all the vertices in the provided graph. This will keep track of all the vertices
    # that have been provided in the 'times' argument to the function. If the length of this does not match the n argument
    # then it is impossible to traverse all the nodes in the graph.
    vertices: Set[int] = set()

    # iterate through the 'times' argument, populating the graph and the vertices
    for time in connections:
        source, destination, weight = time
        graph[source].append((destination, weight))
        vertices.add(source)
        vertices.add(destination)

    # If the starting vertex provided is not in the graph as a source vertex, then it is also impossible to traverse
    # the entire graph from this node, so we exit early
    if k not in graph:
        return -1

    # Keep track of the shortest time found so far to reach each node. Initialize each node to infinity, except node k
    distances: Dict[int, int | float] = {
        i: float("inf") if i != k else 0 for i in range(1, n + 1)
    }

    # Minimum heap to store the smallest item at the top i.e. the vertex with the shortest time to reach, (time, node)
    # We start with the initial node k, which has a time of 0, as that is the node we start with
    min_heap: List[Tuple[int, int]] = [(0, k)]
    heapq.heapify(min_heap)

    # Iterate through the heap
    while min_heap:
        # Pop off the top of the heap to get the current node with the smallest time to reach
        current_time, current_node = heapq.heappop(min_heap)
        # Check if the current time is greater than the distances
        if current_time > distances[current_node]:
            # skip this
            continue

        # Discover the neighbors of the current node
        neighbors = graph[current_node]

        for node, weight in neighbors:
            new_total_time = current_time + weight
            best_recorded_time = distances[node]
            if new_total_time < best_recorded_time:
                distances[node] = new_total_time
                heapq.heappush(min_heap, (new_total_time, node))

    # Keep track of the minimum time so far
    minimum_time = 0
    for node, distance in distances.items():
        if distance == float("inf"):
            return -1
        minimum_time = max(minimum_time, distance)

    return minimum_time


def network_delay_time_2(times: List[List[int]], n: int, k: int) -> int:
    adjacency: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)
    for src, dst, t in times:
        adjacency[src].append((dst, t))

    pq = PriorityQueue()
    pq.put((0, k))
    visited: Set[int] = set()
    delays = 0

    while not pq.empty():
        time, node = pq.get()

        if node in visited:
            continue

        visited.add(node)
        delays = max(delays, time)
        neighbours = adjacency[node]

        for neighbour in neighbours:
            neighbour_node, neighbour_time = neighbour
            if neighbour_node not in visited:
                new_time = time + neighbour_time
                pq.put((new_time, neighbour_node))

    if len(visited) == n:
        return delays

    return -1
