from typing import List
from datastructures.sets.union_find import UnionFind


def min_cost_to_supply_water(n: int, wells: List[int], pipes: List[List[int]]) -> int:
    # Create a list of all edges including virtual source edges
    edges = []

    # Add edges from virtual source (node 0) to each house with well costs
    # This represents the option to build a well at each house
    for i in range(n):
        edges.append((0, i + 1, wells[i]))

    # Add all pipe connections between houses
    for house1, house2, cost in pipes:
        edges.append((house1, house2, cost))

    # Sort all edges by cost (key step in Kruskal's algorithm)
    edges.sort(key=lambda x: x[2])

    # Initialize Union-Find with n+1 nodes (node 0 through n)
    # Node 0 is our virtual water source
    uf = UnionFind(n + 1)

    total_cost = 0
    edges_used = 0

    # Greedily select edges in order of increasing cost
    for house1, house2, cost in edges:
        # Only add this edge if it connects two different components
        if uf.union(house1, house2):
            total_cost += cost
            edges_used += 1
            # We need exactly n edges to connect n+1 nodes into a tree
            if edges_used == n:
                break

    return total_cost


def min_cost_to_supply_water_2(n: int, wells: List[int], pipes: List[List[int]]) -> int:
    edges = [[0, i + 1, wells[i]] for i in range(n)] + pipes
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n + 1)
    total_cost = 0

    for house1, house2, cost in edges:
        if uf.union(house1, house2):
            total_cost += cost

    return total_cost
