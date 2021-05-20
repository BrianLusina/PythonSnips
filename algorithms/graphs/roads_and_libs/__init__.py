from typing import List


def roads_and_libraries(n: int, c_lib: int, c_road: int, cities: List[List[int]]) -> int:
    """

    @param n: number of cities
    @param c_lib: cost to build a library
    @param c_road: cost to build a road
    @param cities: 2D array denoting cities and their neighbours
    @return: minimum cost to build a city
    @rtype int
    """
    # if the cost to build a library is less than the cost to build a road. build the libraries everywhere
    if c_lib <= c_road:
        return c_lib * n

    # otherwise try to add cities to component with a library
    # adj[i] = cities adjacent to i, derived from edge list
    adjacency_list = [[] for _ in range(n)]

    for a, b in cities:
        # convert 1-based indexes to 0-based
        adjacency_list[a - 1].append(b - 1)
        adjacency_list[b - 1].append(a - 1)

    # start with no cities visited
    visited = [False] * n
    minimum_cost = 0

    for c in range(n):
        # starts a floodfill from city c with a library
        if not visited[c]:
            minimum_cost += c_lib
            visited[c] = True

            queue = [[c, j] for j in adjacency_list[c] if not visited[j]]

            while queue:
                i, j = queue.pop(0)

                if not visited[j]:
                    minimum_cost += c_road
                    visited[j] = True
                    queue.extend([j, k] for k in adjacency_list[j] if not visited[k])

    return minimum_cost
