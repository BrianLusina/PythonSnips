class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = dict()

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.map[key] = True

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.map.pop(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.map
