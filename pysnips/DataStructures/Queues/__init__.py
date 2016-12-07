class Queue(object):
    def __init__(self):
        self._storage = {}
        self._start = -1
        self._end = -1

    def enqueue(self, val):
        self._end += 1
        self._storage[self._end] = val

    def dequeue(self):
        # check if there are values
        if self._end > self._start:
            self._start += 1
            next_up = self._storage[self._start]
            self.who_left(self._start)
            del self._storage[self._start]
        return next_up

    def size(self):
        return self._end - self._start

    def who_left(self, val):
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
