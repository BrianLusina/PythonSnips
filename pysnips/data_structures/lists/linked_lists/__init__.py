class Node(object):

    def __init__(self):
        self.data = None
        self.next_node = None

    def set_and_return_Next(self):
        self.next_node = Node()
        return self.next_node

    def get_next(self):
        return self.next_node

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d

class LinkedList(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def build_list(self, array):
        self.head = Node()
        self.head.set_data(array[0])
        self.temp = self.head
        for i in array[1:]:
            self.temp = self.temp.set_and_return_Next()
            self.temp.set_data(i)
            self.tail = self.temp
        return self.head

    def print_list(self):
        temp_node = self.head
        while temp_node!=self.tail:
            print(temp_node.get_data())
            temp_node = temp_node.get_next()
        print(self.tail.get_data())
