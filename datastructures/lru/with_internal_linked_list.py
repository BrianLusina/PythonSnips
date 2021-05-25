class Node:
    def __init__(self, key=0, data=0):
        self.data = data
        self.key = key
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = {}
        self.size = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    @staticmethod
    def __delete_node(node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def __add_to_head(self, node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.lookup:
            node = self.lookup[key]
            data = node.data
            self.__delete_node(node)
            self.__add_to_head(node)
            return data
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            node = self.lookup[key]
            node.data = value
            self.__delete_node(node)
            self.__add_to_head(node)
        else:
            node = Node(key, value)
            self.lookup[key] = node
            if self.size < self.capacity:
                self.size += 1
                self.__add_to_head(node)
            else:
                del self.lookup[self.tail.prev.key]
                self.__delete_node(self.tail.prev)
                self.__add_to_head(node)
