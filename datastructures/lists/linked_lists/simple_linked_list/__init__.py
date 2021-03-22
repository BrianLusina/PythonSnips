# coding=utf-8


class EmptyListException(Exception):
    pass


class Node(object):
    
    def __init__(self, value=None, next_=None):
        self._value = value
        self.next_ = next_
    
    def next(self):
        return self.next_
    
    def value(self):
        return self._value

class LinkedList(object):
    def __init__(self, data=[]):
        self._head = None
        self._len = 0
        [self.push(datum) for datum in data]

    def head(self):
        if self._head is None:
            raise EmptyListException("Can not get head of empty List")
        return self._head
    
    def push(self, value):
        node = Node(value)
        node.next_ = self._head
        self._head = node
        self._len += 1

    def pop(self):
        if self._head is None:
            raise EmptyListException("Can not pop from empty List")
        self._len -= 1
        result = self._head.value()
        self._head = self._head.next()
        return result
    
    def reversed(self):
        return LinkedList(self)
    
    def __len__(self):
        return self._len
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._head is None:
            raise StopIteration()
        value = self._head.value()
        self._head = self._head.next()
        return value
    
    def next(self):
        return self.__next__()