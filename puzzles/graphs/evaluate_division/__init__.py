from typing import List, Dict, Set
Graph = Dict[str, Dict[str, float]]


def calc_equation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    # the key is the node, and the values is a list of tuples where the first element in the tuple is the neighbouring
    # node and the second element is the weight of the edge
    graph: Graph = {}

    # build our graph
    for i in range(len(equations)):
        from_ = equations[i][0]
        to = equations[i][1]

        # from weight to destination, the weight is values[i]
        if from_ in graph:
            graph[from_][to] = values[i]
        else:
            graph[from_] = {to: values[i]}

        # from destination to the source the weight of edge is (1 / values[i])
        if to in graph:
            graph[to][from_] = 1 / values[i]
        else:
            graph[to] = {from_: 1 / values[i]}

    result = [-1.0] * len(queries)

    # traverse from the source to the destination
    for x in range(len(queries)):
        source = queries[x][0]
        destination = queries[x][1]
        visited = set()
        result[x] = dfs(graph, source, destination, visited)

    return result


def dfs(graph: Graph, source: str, destination: str, visited: Set[str]) -> float:
    if source not in graph:
        return -1.0

    if destination in graph[source]:
        return graph[source][destination]

    # mark source as visited
    visited.add(source)

    for k, v in graph[source].items():
        if k not in visited:
            # for all unvisited neighbors of source do dfs. neighbor becomes the source and destination remains the same
            ans = dfs(graph, k, destination, visited)
            if ans != -1.0:
                # if any of the neighbors is not -1 return (edge weight * ans of a neighbor)
                return ans * v

    # all neighbors returned -1, return -1
    return -1.0
