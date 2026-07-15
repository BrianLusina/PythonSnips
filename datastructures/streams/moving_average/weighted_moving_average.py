class WeightedMovingAverage:
    """
    Weight Assignment: The most recent value always gets the maximum weight (self.size), and weights
    decrease as we look further back in time.

    The Denominator: Unlike the simple moving average where you divide by the count, here you divide by the sum of the
    weights applied.

    For a full window of size 3, weights are 3, 2, and 1. Sum = 6.
    Before the window is full, we use a current_denominator to ensure accuracy.

    The WMA is slightly more expensive (O(size) per next() call) because we have to re-sum the weighted values each time.
    If you need O(1) performance for a weighted average, you might look into an Exponential Moving Average (EMA), which
    uses a smoothing factor (α) to give more weight to recent data without needing to store the full history.
    """

    def __init__(self, size: int):
        self.size = size
        self.buffer = [0] * size
        self.head = 0
        self.count = 0
        # The denominator is the sum of weights: 1 + 2 + ... + size
        # Formula: (n * (n + 1)) / 2
        self.denominator = (size * (size + 1)) / 2

    def next(self, val: int) -> float:
        # 1. Update the buffer
        self.buffer[self.head] = val
        self.head = (self.head + 1) % self.size
        if self.count < self.size:
            self.count += 1

        # 2. Calculate Weighted Sum
        weighted_sum = 0.0
        current_denominator = 0

        # Iterate backward from the most recent element
        for i in range(self.count):
            # Find index of elements from newest to oldest
            # (self.head - 1 - i) handles the circular wrap-around
            idx = (self.head - 1 - i) % self.size
            weight = self.size - i
            weighted_sum += self.buffer[idx] * weight
            current_denominator += weight

        return weighted_sum / current_denominator
