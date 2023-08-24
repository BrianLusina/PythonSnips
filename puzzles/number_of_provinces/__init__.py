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
