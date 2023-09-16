from typing import List, Dict, Set

Graph = Dict[str, Dict[str, float]]


def calc_equation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    # the key is the node, and the values is a list of tuples where the first element in the tuple is the neighbouring
    # node and the second element is the weight of the edge

    # build our graph
    graph = build_graph(equations=equations, values=values)

    result = []

    # traverse from the source to the destination
    for query in queries:
        source, destination = query
        if source not in graph or destination not in graph:
            result.append(-1.0)
        else:
            visited = set()
            ans = [-1.0]
            temp = 1.0
            dfs(graph, source, destination, visited, ans, temp)
            result.append(ans[0])

    return result


def build_graph(equations: List[List[str]], values: List[float]) -> Graph:
    # the key is the node, and the values is a list of tuples where the first element in the tuple is the neighbouring
    # node and the second element is the weight of the edge
    graph: Graph = {}

    # build our graph
    for i in range(len(equations)):
        from_, to = equations[i]
        value = values[i]

        # from weight to destination, the weight is values[i]
        if from_ in graph:
            graph[from_][to] = value
        else:
            graph[from_] = {to: value}

        # from destination to the source the weight of edge is (1 / values[i])
        if to in graph:
            graph[to][from_] = 1 / value
        else:
            graph[to] = {from_: 1 / value}

    return graph


def dfs(graph: Graph, source: str, destination: str, visited: Set[str], ans: List[float], temp: float):
    if source in visited:
        return

    # mark source as visited
    visited.add(source)

    if source == destination:
        ans[0] = temp
        return

    for k, v in graph[source].items():
        # for all unvisited neighbors of source do dfs. neighbor becomes the source and destination remains the same
        dfs(graph, k, destination, visited, ans, temp * v)
