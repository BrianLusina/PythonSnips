class Queue(object):
    """
    Queue implementation in Python
    Methods:
        enqueue adds an item to the queue
        dequeue removes an item from the front of the queue
        size returns the size of the queue
        peek returns the element at the front of the queue, without removing it
        is_full checks if the queue is full
        is_empty checks if the queue is empty
    """
    def __init__(self):
        self.queue = []
        self._storage = {}
        self._start = -1
        self._end = -1

    def enqueue(self, val):
        """
        Adds item to the end of the queue
        :param val:
        :return:
        """
        self.queue.append(val)
        self._end += 1
        self._storage[self._end] = val

    def dequeue(self):
        """
        Removes an item from the fron of the queue
        :return:
        """
        # check if there are values
        if self._end > self._start:
            self._start += 1
            next_up = self._storage[self._start]
            self.who_left(self._start)
            del self._storage[self._start]
        return next_up

    def size(self):
        return self._end - self._start

    @staticmethod
    def who_left(val):
        """
        Notifies who left queue
        :return: *User* Object
        :rtype object
        """
        return str(val)

    def __repr__(self):
        return "Start: %r End: %r Size: %r, \n Queue:%r" % (self._start, self._end, self.size(), self._storage)


class User(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return "{Name: %r, Email: %r, Phone:%r}" % (self.name, self.email, self.phone)
