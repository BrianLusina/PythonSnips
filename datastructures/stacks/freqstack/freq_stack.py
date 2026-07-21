from abc import ABC
from datastructures.stacks import Stack, T
from collections import defaultdict


class FreqStack(Stack, ABC):
    """
    A stack-like data structure that pops the most/least frequently occurring element.
    When multiple elements have the same frequency, the most recently pushed element is popped.
    """

    def __init__(self):
        """Initialize the frequency stack with necessary data structures"""
        # Dictionary to keep track of the frequency of each element
        self.frequency_count = defaultdict(int)
        self.priority_queue = []
        self.timestamp = 0

    def peek(self) -> T:
        if len(self.priority_queue) == 0:
            return None
        return self.priority_queue[0][2]

    def is_empty(self) -> bool:
        return len(self.priority_queue) == 0
