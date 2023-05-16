from .. import Node


class SingleNode(Node):
    """
    SingleNode implementation in a single linked list
    """

    def __init__(self, value, next_=None):
        super().__init__(value, next_)
        self.data = value
        self.next = next_

