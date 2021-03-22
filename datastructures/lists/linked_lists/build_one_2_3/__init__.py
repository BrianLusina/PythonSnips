class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    node = Node(data)
    node.next = head
    return node


def build_one_two_three():
    return push(push(Node(3), 2), 1)
