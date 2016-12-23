class LinkedList(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def buildList(self, array):
        self.head = Node()
        self.head.setData(array[0])
        self.temp = self.head
        for i in array[1:]:
            self.temp = self.temp.set_and_return_Next()
            self.temp.setData(i)
            self.tail = self.temp
        return self.head

    def printList(self):
        tempNode = self.head
        while(tempNode!=self.tail):
            print(tempNode.getData())
            tempNode = tempNode.getNext()
        print(self.tail.getData())
