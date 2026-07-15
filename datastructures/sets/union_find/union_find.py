class UnionFind:
    """A minimal Union-Find data structure with path compression."""

    def __init__(self, size: int):
        """Initializes the data structure with 'size' elements."""
        if size <= 0:
            raise ValueError("Size must be a positive integer.")
        self.parent = list(range(size))

    def find(self, x: int) -> int:
        """Finds the representative (root) of the set containing element 'x'."""
        if self.parent[x] != x:
            # Path compression
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        Merges the sets containing elements 'x' and 'y'.
        Returns True if a merge occurred, False if already in same set.
        """
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x
            return True
        return False
