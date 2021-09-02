from queue import Queue


def shortest_path_(graph: dict, start_node, end_node):
    """
    Find the shortest path in the graph from the start_node to the end_node
    This will use Breadth-First-Search(BFS) as it allows finding the shortest path in a graph although takes up more memory
    than Depth-First-Search. We will use a set to track the nodes we have already traversed to prevent repeating our search and 
    also speeding up the search for the shortest path

    We're using a queue instead of a list because we want an efficient first-in-first-out (FIFO) structure with O(1) inserts and removes.
    If we used a list, appending would be O(1), but removing elements from the front would be O(n).

    """
    if start_node not in graph:
        raise Exception("Start node not in Graph")

    if end_node not in graph:
        raise Exception("End node not in graph")

    nodes_to_visit = Queue()
    nodes_to_visit.put(start_node)

    # keep track of how we got to each node
    # we'll use this to reconstruct the shortest path at the end
    # we'll ALSO use this to keep track of which nodes we've
    # already visited
    how_we_reached_nodes = {start_node: None}

    while not nodes_to_visit.empty():
        current_node = nodes_to_visit.get()

        if current_node == end_node:
            return reconstruct_path(how_we_reached_nodes, start_node, end_node)

        for neighbor in graph[current_node]:
            if neighbor not in how_we_reached_nodes:
                how_we_reached_nodes[neighbor] = current_node
                nodes_to_visit.put(neighbor)

    # if we get here, then we never found the end node
    # so there's NO path from start_node to end_node
    return None


def reconstruct_path(how_we_reached_nodes: dict, start_node, end_node):
    shortest_path = []

    # start from the end node(recipient) and work backwards
    current_node = end_node

    while current_node:
        shortest_path.append(current_node)

        current_node = how_we_reached_nodes[current_node]

    # we reverse, because start from the recipients node instead of the senders node
    shortest_path.reverse()

    return shortest_path
