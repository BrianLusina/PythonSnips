from collections import defaultdict, deque
from typing import List, Dict, Deque

WHITE = 1
GRAY = 2
BLACK = 3


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    This function finds the topological sorted order of the courses given the prerequisites.

    Args:
        num_courses (int): The total number of courses.
        prerequisites (List[List[int]]): A list of tuples where each tuple contains the source and destination of the prerequisite.

    Returns:
        List[int]: A list of the courses in the topological sorted order. If there is no valid order, return an empty list.

    """
    adjacency_list = defaultdict(list)

    # Populate the adjacency list with the prerequisites
    for destination, source in prerequisites:
        adjacency_list[source].append(destination)

    topological_sorted_order = []
    is_possible = True

    # Use a dictionary to keep track of the color of each node
    color = {k: WHITE for k in range(num_courses)}

    def dfs(node):
        """
        This function performs a depth-first search on the graph.

        Args:
            node (int): The current node being visited.

        Returns:
            None

        """
        nonlocal is_possible

        # If there is no valid order, return immediately
        if not is_possible:
            return

        # Mark the current node as gray
        color[node] = GRAY

        # If the current node has any neighbours, visit them
        if node in adjacency_list:
            for neighbour in adjacency_list[node]:
                # If the neighbour is white, visit it
                if color[neighbour] == WHITE:
                    dfs(neighbour)
                # If the neighbour is gray, there is no valid order
                elif color[neighbour] == GRAY:
                    is_possible = False

        # Mark the current node as black
        color[node] = BLACK
        topological_sorted_order.append(node)

    # Visit all the nodes
    for vertex in range(num_courses):
        if color[vertex] == WHITE:
            dfs(vertex)

    # If there is no valid order, return an empty list
    return topological_sorted_order[::-1] if is_possible else []


def can_finish(
    num_courses: int,
    prerequisites: List[List[int]]
) -> bool:
    """
    Determines if there is a valid order of courses such that
    all prerequisites are satisfied.

    Args:
        num_courses (int): The total number of courses.
        prerequisites (List[List[int]]): A list of tuples where each tuple contains the source and destination of the prerequisite.

    Returns:
        bool: True if there is a valid order, False otherwise.
    """
    counter: int = 0
    if num_courses <= 0:
        return True

    # Initialize the in-degree of all nodes to 0
    in_degree: Dict[int, int] = {i: 0 for i in range(num_courses)}
    # Initialize an adjacency list to store the graph
    graph: Dict[int, List[int]] = {i: [] for i in range(num_courses)}

    # Populate the adjacency list and the in-degree of all nodes
    for child, parent in prerequisites:
        if parent in graph:
            graph[parent].append(child)
        else:
            graph[parent] = [child]
        if child in in_degree:
            in_degree[child] += 1
        else:
            in_degree[child] = 1

    # Initialize a queue to store all nodes with an in-degree of 0
    sources: Deque[int] = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    # Perform a BFS traversal of the graph
    while sources:
        course: int = sources.popleft()
        counter += 1
        for child in graph[course]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    # If all nodes have been visited, return True
    return counter == num_courses