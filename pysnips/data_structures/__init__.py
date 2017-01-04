from pysnips.data_structures.stacks import Stack
from pysnips.data_structures.queues import Queue


class DataStructures(object):
    """
    implementation of various data structure implementations. May contain mixes of data structures
    """
    def __init__(self):
        pass

    class QueueTwoStacks(object):
        """
        Queues two stacks
        """
        def __init__(self, stack_size):
            self.in_stack = Stack(stack_size)
            self.out_stack = Stack(stack_size)

        def enqueue(self, item):
            """
            Adds an item to the bottom of in_stack
            :param item: Item to add to in_stack
            :return None
            """
            self.in_stack.push(item)

        def dequeue(self):
            """
            Removes and returns the top most item from out_stack. This will involve moving items from in_stack to
            out_stack in order to reverse their order and return the oldest item from in_stack(which is at the bottom
            of in_stack)
            :return: Item at the top of out_stack
            """
            if self.out_stack.get_len() == 0:
                # move items from in_stack to out_stack, reversing order
                while self.in_stack.get_len() > 0:
                    newest_in_stack_item = self.in_stack.pop()
                    self.out_stack.push(newest_in_stack_item)
                # if out_stack is still empty, raise an error
                if self.out_stack.get_len() == 0:
                    raise IndexError("Can't dequeue from empty Queue")
            return self.out_stack.pop()
