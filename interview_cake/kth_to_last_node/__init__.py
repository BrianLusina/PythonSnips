class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return "Value: %r, <Next: %r>" % (self.value, self.next)
