class MovingAverageWithBuffer:
    """
    Using a Circular Buffer (implemented with a fixed-size list) is an excellent way to optimize memory. Instead of
    dynamically resizing or shifting elements, we use a fixed array and a pointer that "wraps around" using the modulo
    operator (index(modsize)).

    This approach is often preferred in embedded systems or high-performance scenarios because it avoids the overhead of
     frequent memory allocations.

     The expression self.head = (self.head + 1) % self.size ensures that if our size is 3, the pointer sequence will be:
     0 → 1 → 2 → 0 → 1...

     This effectively "recycles" the array positions, making it behave like a continuous loop.
    """

    def __init__(self, size: int):
        # Pre-allocate a list of zeros
        self.size = size
        self.buffer = [0] * size
        self.head = 0  # Pointer to the next position to overwrite
        self.count = 0  # Track how many elements we've actually added
        self.current_sum = 0.0

    def next(self, val: int) -> float:
        # If the buffer is full, subtract the value we are about to overwrite
        if self.count == self.size:
            self.current_sum -= self.buffer[self.head]
        else:
            self.count += 1

        # Overwrite the old value at the head pointer
        self.buffer[self.head] = val
        self.current_sum += val

        # Move the pointer to the next index, wrapping around if at the end
        self.head = (self.head + 1) % self.size

        return self.current_sum / self.count
