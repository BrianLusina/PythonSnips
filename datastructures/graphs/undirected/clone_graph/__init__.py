from typing import Optional, Dict
from datastructures.graphs.undirected.clone_graph.node import Node


def clone(root: Optional[Node]) -> Optional[Node]:
    def clone_helper(n: Optional[Node], nodes_cloned: Dict[Node, Node]) -> Optional[Node]:
        # If the node is None, return None
        if n is None:
            return None

        # Create a new Node with the same data as the node
        cloned_node = Node(n.data)
        # Add the node and its clone to the nodes_completed hash map
        nodes_cloned[n] = cloned_node

        # Iterate through the neighbours of the node
        for neighbour in n.neighbors:
            # Retrieve the value of key neighbour in nodes_completed hash map.
            # If it exists, assign the corresponding cloned node to cloned_neighbour.
            # This checks if the neighbour node neighbour has already been cloned.
            cloned_neighbour = nodes_cloned.get(neighbour)
            # If the neighbour is not cloned yet, recursively clone it
            if not cloned_neighbour:
                cloned_node.neighbors += [clone_helper(neighbour, nodes_cloned)]
            # If the neighbour is already cloned, add the cloned neighbour to the new
            # node's neighbors
            else:
                cloned_node.neighbors += [cloned_neighbour]
        return cloned_node

    # Initialize an empty dictionary to keep track of cloned nodes
    nodes_completed: Dict[Node, Node] = {}
    # Call the recursive function to clone the graph starting from the root node
    return clone_helper(root, nodes_completed)
