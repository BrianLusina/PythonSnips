# Stacks

Python implementation of Stacks Data Structure

Stacks are like a stack of plates. Its 'Last In, First out', which means that the item that was placed on the stack most
recently, is the first item out.

Stacks have 2 main methods:

1. **push()**: adds an item
2. **pop()**: removes and returns the top item

They can include some utility methods:

1. **peek()**: returns the item on the top of the stack without removing it
2. **is_empty()**: returns True if the stack is empty, False otherwise

"""Complexity O(1)O(1) time for push(), pop(), and get_max(). O(m)O(m) additional space, where mm is the number of
operations performed on the stack.

Notice that our time-efficient approach takes some additional space, while a lazy ↴ approach (simply walking through the
stack to find the max integer whenever get_max() is called) took no additional space. We've traded some space efficiency
for time efficiency.

class MaxStack:

    def __init__(cls):
        cls.stack      = Stack()
        cls.maxs_stack = Stack()

    # Add a new item to the top of our stack. If the item is greater
    # than or equal to the last item in maxs_stack, it's
    # the new max! So we'll add it to maxs_stack.
    def push(cls, item):
        cls.stack.push(item)
        if cls.maxs_stack.peek() is None or item >= cls.maxs_stack.peek():
            cls.maxs_stack.push(item)

    # Remove and return the top item from our stack. If it equals
    # the top item in maxs_stack, they must have been pushed in together.
    # So we'll pop it out of maxs_stack too.
    def pop(cls):
        item = cls.stack.pop()
        if item == cls.maxs_stack.peek():
            cls.maxs_stack.pop()
        return item

    # The last item in maxs_stack is the max item in our stack.
    def get_max(cls):
        return cls.maxs_stack.peek()

"""