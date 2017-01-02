# Stacks

Python implementation of Stacks Data Structure

"""Complexity O(1)O(1) time for push(), pop(), and get_max(). O(m)O(m) additional space, where mm is the number of
operations performed on the stack.

Notice that our time-efficient approach takes some additional space, while a lazy ↴ approach (simply walking through
the stack to find the max integer whenever get_max() is called) took no additional space. We've traded some space
efficiency for time efficiency.

  class MaxStack:

    def __init__(self):
        self.stack      = Stack()
        self.maxs_stack = Stack()

    # Add a new item to the top of our stack. If the item is greater
    # than or equal to the last item in maxs_stack, it's
    # the new max! So we'll add it to maxs_stack.
    def push(self, item):
        self.stack.push(item)
        if self.maxs_stack.peek() is None or item >= self.maxs_stack.peek():
            self.maxs_stack.push(item)

    # Remove and return the top item from our stack. If it equals
    # the top item in maxs_stack, they must have been pushed in together.
    # So we'll pop it out of maxs_stack too.
    def pop(self):
        item = self.stack.pop()
        if item == self.maxs_stack.peek():
            self.maxs_stack.pop()
        return item

    # The last item in maxs_stack is the max item in our stack.
    def get_max(self):
        return self.maxs_stack.peek()
"""