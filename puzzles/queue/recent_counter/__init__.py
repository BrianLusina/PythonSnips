from collections import deque


class RecentCounter:
    def __init__(self):
        self.sliding_window = deque()

    def ping(self, t: int) -> int:
        self.sliding_window.append(t)

        while self.sliding_window[0] < t - 3000:
            self.sliding_window.popleft()

        return len(self.sliding_window)
