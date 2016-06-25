class Node:

    def __init__(self):
        self.data = None
        self.nextNode = None

    def set_and_return_Next(self):
        self.nextNode = Node()
        return self.nextNode

    def getNext(self):
        return self.nextNode

    def getData(self):
        return self.data

    def setData(self, d):
        self.data = d

class LinkedList:

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

myArray = [3, 5, 4, 6, 2, 6, 7, 8, 9, 10, 21]

myList = LinkedList()
myList.buildList(myArray)
myList.printList()