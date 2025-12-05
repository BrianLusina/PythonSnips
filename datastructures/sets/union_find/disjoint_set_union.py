class DisjointSetUnion:
    """A class for the Union-Find (Disjoint Set Union) data structure."""

    def __init__(self, size: int):
        """Initializes the data structure with 'size' elements, each in its own set."""
        if size <= 0:
            raise ValueError("Size must be a positive integer.")
        self.root = list(range(size))
        self.rank = [1] * size  # For union by rank
        self.count = size  # Number of disjoint sets

    def find(self, i: int) -> int:
        """Finds the representative (root) of the set containing element 'i'."""
        if self.root[i] == i:
            return i
        # Path compression: make all nodes on the path point to the root
        self.root[i] = self.find(self.root[i])
        return self.root[i]

    def union(self, i: int, j: int) -> bool:
        """
        Merges the sets containing elements 'i' and 'j'.
        Returns True if a merge occurred, False if they were already in the same set.
        """
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Union by rank: attach the smaller tree to the larger tree
            if self.rank[root_i] > self.rank[root_j]:
                self.root[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.root[root_i] = root_j
            else:
                self.root[root_j] = root_i
                self.rank[root_i] += 1

            self.count -= 1
            return True

        return False

    def get_count(self) -> int:
        """Returns the current number of disjoint sets."""
        return self.count
