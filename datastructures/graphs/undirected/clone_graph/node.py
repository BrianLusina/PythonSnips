from typing import Any, List


class Node:
    def __init__(self, d: Any):
        self.data: Any = d
        self.neighbors: List["Node"] = []
