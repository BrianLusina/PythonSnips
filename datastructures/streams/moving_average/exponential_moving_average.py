class ExponentialMovingAverage:
    """
    The Exponential Moving Average (EMA) is widely used in finance and signal processing because it reacts faster to
    recent price changes than a simple moving average.

    The beauty of the EMA is its efficiency: it does not require a buffer or a window of previous values. You only need
    to store the previous EMA result. This makes the time and space complexity both O(1).

    Why use EMA?
    1. Reduced Lag: Because it weights the most recent data most heavily, it catches trend reversals much sooner than an SMA.
    2. Memory Efficiency: You don't need to store a list of numbers; you only need to store one variable (self.ema).
    3. Smoothness: It creates a smooth curve that isn't as sensitive to an old "outlier" dropping out of the window (a common issue with SMA).
    """

    def __init__(self, size: int):
        self.size = size
        self.alpha = 2 / (size + 1)
        self.ema = None  # Initialized with the first value received

    def next(self, val: int) -> float:
        if self.ema is None:
            # The first value acts as the starting point
            self.ema = float(val)
        else:
            # Apply the EMA formula
            self.ema = (val * self.alpha) + (self.ema * (1 - self.alpha))

        return self.ema
