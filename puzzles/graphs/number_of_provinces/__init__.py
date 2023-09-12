from typing import List


class UnionFind:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size

    def find(self, x: int) -> int:
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        x_root, y_root = self.find(x), self.find(y)

        if x_root == y_root:
            return

        if self.rank[x_root] < self.rank[y_root]:
            self.root[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.root[y_root] = x_root
        else:
            self.root[y_root] = x_root
            self.rank[x_root] += 1
            self.count -= 1


def number_of_provinces(grid: List[List[int]]) -> int:
    """
    returns the number of provinces given a grid showing whether cities are connected or not
    @param grid: grid showing connection between cities
    @return: number of provinces
    """
    if not grid or len(grid) == 0:
        return 0

    n_rows = len(grid)
    uf = UnionFind(n_rows)

    for row in range(n_rows):
        for col in range(row + 1, n_rows):
            if grid[row][col] == 1:
                uf.union(row, col)

    return uf.count


def number_of_provinces_dfs(is_connected: List[List[int]]) -> int:
    """Finds the number of connected components(graphs) in a given adjacency list is_connected. Uses DFS traversal
    algorithm to find the connected components or the number of graphs from the provided 2D array.

    Complexity:
    - Time Complexity: O(n^2).
        Initializing the visited array takes O(n) time.
        The dfs function visits each node once, which takes O(n) time because there are n nodes in total.
        From each node, we iterate over all possible edges using graph[node] which takes O(n) time for each visited node.
        As a result, it takes a total of O(n^2) time to visit all the nodes and iterate over its edges.

    - Space Complexity: O(n)
        visited array takes O(n) space
        Recursion call stack used by dfs can have no more than n elements in the worst case. It would take up to O(n)
        space in that case.

    Args:
        is_connected(list): 2D Array denoting an adjacency list where the index is a city and the values at that index
        denote interconnectivity with 1 showing a direct connection and 0 showing no connection

    Return:
        int: Number of connected components or number of graphs from the list
    """
    number_of_cities = len(is_connected)
    provinces = 0
    # keeps track of visited cities
    visited = [False] * number_of_cities

    def dfs(node: int, graph: List[List[int]], visit: List[bool]):
        # mark this node as visited/or mark this city as visited
        visit[node] = True
        for i in range(len(graph)):
            # get the city's neighbour to check if it can be reached, in this case if the value is 1, we can reach
            # city's neighbour, i.e, they are connected
            neighbour = graph[node][i]

            # Checks if the neighbour has already been visited
            neighbour_visited = visit[i]

            if neighbour == 1 and not neighbour_visited:
                # if the city is connected to this current city(node) and we have not yet visited it, we continue
                # with traversal
                dfs(i, graph, visit)

    for city in range(number_of_cities):
        # if city has not been visited
        if not visited[city]:
            # increment number of provinces
            provinces += 1
            # perform a dfs from the city to other cities
            dfs(city, is_connected, visited)

    return provinces
