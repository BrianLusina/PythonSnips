from typing import Deque
from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        """
        Initializes the moving average object
        Args:
            size (int): The size of the moving average
        """
        self.queue: Deque[int] = deque()
        self.size: int = size
        self.window_sum: float = 0.0

    def next(self, val: int) -> float:
        """
        Adds a value to the stream and returns the moving average of the stream
        Args:
            val (int): The value to add to the stream
        Returns:
            float: The moving average of the stream
        """
        if len(self.queue) == self.size:
            # remove oldest value
            oldest_value = self.queue.popleft()
            self.window_sum -= oldest_value

        # add new value to queue
        self.queue.append(val)
        self.window_sum += val

        # calculate average
        return self.window_sum / len(self.queue)
