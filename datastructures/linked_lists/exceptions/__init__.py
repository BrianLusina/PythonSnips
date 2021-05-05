class NodeDoesNotExist(Exception):
    def __init__(self, message=None):
        if message is None:
            message = "Node does not exist"
        super(NodeDoesNotExist, self).__init__(message)


class EmptyLinkedList(Exception):
    def __init__(self, message=None):
        if message is None:
            message = "LinkedList is empty"
        super(EmptyLinkedList, self).__init__(message)
