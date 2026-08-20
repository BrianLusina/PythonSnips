from typing import List
from collections import defaultdict, deque


def collect_the_coins(coins: List[int], edges: List[List[int]]) -> int:
    # Build the adjacency list representation of the tree
    graph = defaultdict(set)
    for node_a, node_b in edges:
        graph[node_a].add(node_b)
        graph[node_b].add(node_a)

    n = len(coins)

    # Remove all leaf nodes that don't have coins. Initialize a queue with leaf nodes(degree 1) that have no coins
    queue = deque(
        node for node in range(n) if len(graph[node]) == 1 and coins[node] == 0
    )

    # Keep removing leaf nodes without coins
    while queue:
        current_node = queue.popleft()

        # Remove this node from its neighbor's adjacency list
        for neighbor in graph[current_node]:
            graph[neighbor].remove(current_node)
            # If neighbor becomes a leaf node and has no coin, add to queue
            if coins[neighbor] == 0 and len(graph[neighbor]) == 1:
                queue.append(neighbor)
        # Clear the current node's connections
        graph[current_node].clear()

    # Remove two layers of lead nodes. This accounts for the collection distance of 2
    for layer in range(2):
        # Find all current leaf nodes
        leaf_nodes = [node for node in range(n) if len(graph[node]) == 1]
        # Remove all leaf nodes from the adjacency list
        for leaf in leaf_nodes:
            for neighbour in graph[leaf]:
                graph[neighbour].remove(leaf)
            graph[leaf].clear()

    # Count remaining edgest that need to be traversed. An edge is counted if both its endpoints still exist in the graph
    # Multiply by 2 because we need to traverse each edge twice (forward and back)
    remaining_edges = sum(
        len(graph[node_a]) > 0 and len(graph[node_b]) > 0 for node_a, node_b in edges
    )

    return remaining_edges * 2


def collect_the_coins_2(coins: List[int], edges: List[List[int]]) -> int:
    # Get the number of nodes
    n = len(coins)

    # Build adjacency set for each node (using sets for O(1) removal)
    graph = [set() for _ in range(n)]
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)

    # --- Phase 1: Topological sort to remove non-coin leaves ---
    # Initialize queue with leaf nodes that have no coins
    queue = deque()
    for node in range(n):
        # A leaf is a node with exactly one neighbor
        if len(graph[node]) == 1 and coins[node] == 0:
            queue.append(node)

    # Repeatedly prune zero-coin leaves
    while queue:
        node = queue.popleft()
        # For the single neighbor of this leaf
        for neighbor in graph[node]:
            graph[neighbor].discard(node)
            # If neighbor becomes a no-coin leaf, add to queue
            if len(graph[neighbor]) == 1 and coins[neighbor] == 0:
                queue.append(neighbor)
        # Remove all edges from this node
        graph[node].clear()

    # --- Phase 2: Prune two layers of leaves from the remaining tree ---
    # First layer pruning: remove current coin-bearing leaves
    for _ in range(2):
        leaf_nodes = [node for node in range(n) if len(graph[node]) == 1]
        for node in leaf_nodes:
            for neighbor in graph[node]:
                graph[neighbor].discard(node)
            graph[node].clear()

    # --- Result: count remaining edges * 2 ---
    # Each remaining edge must be traversed twice (once each way)
    remaining_edges = sum(len(neighbors) for neighbors in graph) // 2
    return remaining_edges * 2
