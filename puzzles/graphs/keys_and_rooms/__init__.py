from typing import List
from collections import deque


def can_visit_all_rooms(rooms: List[List[int]]) -> bool:
    """ Checks if it's possible to visit all rooms if we have only the 1st room as open. The input rooms is a 2D array/
    matrix with all the rooms with each room's number as the index and the value at each index being the list of keys
    for other room numbers.

    Space Complexity: O(n+k) as we are keeping track of visited nodes in a set and k is the number of keys.
    Time Complexity: O(n) as we are traversing all nodes in the graph

    Args:
        rooms (list): adjacency list where room[i] represents the adjacent vertices of the vertex i.

    Returns:
         bool: indicating whether it is possible to visit all the vertices/rooms in the adjacency list
    """
    # if there are no rooms, then return False
    if len(rooms) == 0:
        return False

    # keep track of all visited nodes.
    # Space complexity is O(n) where is is all the vertices in the graph
    visited_nodes = set()

    # all vertices awaiting processing
    # Space complexity is O(n) where we keep track of vertices awaiting processing, where n is the number of vertices
    # in the graph
    queue = deque([])

    # starting node is 0. Note that this is the index in the rooms. Here it denotes the starting vertex.
    starting_node = 0

    # since we start at the starting node, this node is added to visited nodes and the queue for processing
    visited_nodes.add(starting_node)
    queue.append(starting_node)

    while queue:
        # dequeue the vertex from the queue
        vertex = queue.popleft()

        # get all the vertex adjacent neighbors, i.e. rooms we can visit from current room
        neighbours = rooms[vertex]

        # for each neighbour
        for neighbour in neighbours:
            # check if we haven't visited this room
            if neighbour not in visited_nodes:
                # add it for processing
                queue.append(neighbour)
                # add that we have visited this node
                visited_nodes.add(neighbour)

    # At this point, the length of visited nodes should equal to the initial length of rooms. if the length is not equal
    # it means it is not possible to visit all the rooms from the starting room
    return len(visited_nodes) == len(rooms)
