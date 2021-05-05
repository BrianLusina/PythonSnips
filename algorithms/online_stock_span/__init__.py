from datastructures.stacks import Stack


class StockSpanner:

    def __init__(self):
        self.stack = Stack()

    def next(self, price: int) -> int:
        weight = 1

        while not self.stack.is_empty() and self.stack.peek()[-1][0] <= price:
            weight += self.stack.pop()[1]

        self.stack.push((price, weight))
        return weight
