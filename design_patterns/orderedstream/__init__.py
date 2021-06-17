from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.stream = [None] * (n + 1)
        self.pointer = 1

    def insert(self, id_key: int, value: str) -> List[str]:
        self.stream[id_key] = value

        if id_key > self.pointer:
            return []

        while self.pointer < len(self.stream) and self.stream[self.pointer]:
            self.pointer += 1
        return self.stream[id_key: self.pointer]
