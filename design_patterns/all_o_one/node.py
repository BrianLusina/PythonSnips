from typing import Any


class Node:
    def __init__(self, freq: Any):
        self.freq = freq
        self.next = None
        self.previous = None
        self.keys = set()
