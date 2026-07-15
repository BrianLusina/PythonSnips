from typing import List, Set
from datastructures import UnionFind


def count_components_union_find(n: int, edges: List[List[int]]) -> int:
    """
    Count the number of connected components in an undirected graph.

    Args:
        n: Number of nodes (labeled from 0 to n-1)
        edges: List of edges where each edge is [node1, node2]

    Returns:
        Number of connected components in the graph
    """
    # Create an instance of Disjoint Set/Union Find to track connected components
    dsu = UnionFind(n)

    # initialize the result to the total number of nodes initially
    res = n

    # iterate through each edge (node_a, node_b) in the `edges` list
    for node_a, node_b in edges:
        # If nodes node_a and node_b are not already connected, perform the union operation
        if dsu.union(node_a, node_b):
            # Decrease the result by 1, indicating that the two separate `components` have been merged
            res -= 1

    return res


def count_components_dfs(n: int, edges: List[List[int]]) -> int:
    """
    Count the number of connected components in an undirected graph.

    Args:
        n: Number of nodes (labeled from 0 to n-1)
        edges: List of edges where each edge is [node1, node2]

    Returns:
        Number of connected components in the graph
    """
    # Build an adjacency list representing the graph
    adjacency_list = [[] for _ in range(n)]
    for node_a, node_b in edges:
        adjacency_list[node_a].append(node_b)
        adjacency_list[node_b].append(node_a)

    # Track visited nodes. Using a set gives us the advantage of O(1) lookup time as opposed to using an array
    visited: Set[int] = set()

    def dfs(node: int) -> int:
        """
        Depth-first search to mark all nodes in a connected component.

        Args:
            node: Current node to visit

        Returns:
            1 if this node starts a new component, 0 if already visited
        """
        # If the node was already visited, it's part of a previously counted component
        if node in visited:
            return 0
        # Mark the current node as visited
        visited.add(node)
        # Visit all neighbors of the current node
        for neighbor in adjacency_list[node]:
            dfs(neighbor)
        # Return 1 to indicate a new component was found
        return 1

    # Count components by starting DFS from each unvisited nodes
    total = sum(dfs(node) for node in range(n))

    return total


def count_components_dfs_iterative(n: int, edges: List[List[int]]) -> int:
    """
    Count the number of connected components in an undirected graph.

    Args:
        n: Number of nodes (labeled from 0 to n-1)
        edges: List of edges where each edge is [node1, node2]

    Returns:
        Number of connected components in the graph
    """
    # Build an adjacency list representing the graph
    adjacency_list = [[] for _ in range(n)]
    for node_a, node_b in edges:
        adjacency_list[node_a].append(node_b)
        adjacency_list[node_b].append(node_a)

    # Track visited nodes. Using a set gives us the advantage of O(1) lookup time as opposed to using an array
    visited: Set[int] = set()

    def dfs(start: int) -> int:
        """
        Depth-first search to mark all nodes in a connected component.

        Args:
            start: Current node to visit

        Returns:
            1 if this node starts a new component, 0 if already visited
        """
        # If the node was already visited, it's part of a previously counted component
        if start in visited:
            return 0

        stack = [start]

        while stack:
            node = stack.pop()
            if node in visited:
                continue
            # Mark the current node as visited
            visited.add(node)
            # Visit all neighbors of the current node
            for neighbor in adjacency_list[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

        # Return 1 to indicate a new component was found
        return 1

    # Count components by starting DFS from each unvisited nodes
    total = sum(dfs(node) for node in range(n))

    return total
