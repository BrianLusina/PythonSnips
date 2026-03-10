from datastructures.linked_lists.doubly_linked_list.node import DoubleNode


class LfuCacheNode(DoubleNode):
    def __init__(self, data, key):
        super().__init__(data, key=key)
        self.frequency = 1


class LfuCacheNodeV2(DoubleNode):
    def __init__(self, data, key):
        super().__init__(data, key=key)
        self.frequency = 0
