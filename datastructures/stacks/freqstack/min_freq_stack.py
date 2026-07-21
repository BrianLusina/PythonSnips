from datastructures.stacks import T
from heapq import heappush, heappop
from datastructures.stacks.freqstack.freq_stack import FreqStack


class MinFreqStack(FreqStack):
    """
    A stack-like data structure that pops the least frequently occurring element.
    When multiple elements have the same frequency, the least recently pushed element is popped.
    """

    def push(self, item: T):
        # Increment the timestamp for this operation
        self.timestamp += 1
        # Update the frequency count
        self.frequency_count[item] += 1
        heappush(
            self.priority_queue, (self.frequency_count[item], self.timestamp, item)
        )

    def pop(self) -> T:
        """
        Pop and return the most frequent element from the stack. If there is a tie in frequency, return the recently
        pushed element.
        """
        # Extract the value with the highest priority(most frequent, most recent)
        _, _, value = heappop(self.priority_queue)
        # Decrease the frequency count for this value
        self.frequency_count[value] -= 1
        return value
