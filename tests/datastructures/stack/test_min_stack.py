import unittest

from datastructures.stacks.minstack import MinStack


class MinStackTestCases(unittest.TestCase):
    def test_one(self):
        min_stack = MinStack()
        min_stack.push(-2)

        self.assertEqual([-2], list(min_stack.stack))

        min_stack.push(0)

        self.assertEqual([-2, 0], list(min_stack.stack))

        min_stack.push(-3)

        self.assertEqual([-2, 0, -3], list(min_stack.stack))

        actual_current_min_1 = min_stack.get_min()

        self.assertEqual([-2, 0, -3], list(min_stack.stack))
        self.assertEqual(-3, actual_current_min_1)

        min_stack.pop()

        self.assertEqual([-2, 0], list(min_stack.stack))

        current_top = min_stack.peek()

        self.assertEqual(0, current_top)
        self.assertEqual([-2, 0], list(min_stack.stack))

        actual_current_min_2 = min_stack.get_min()

        self.assertEqual([-2, 0], list(min_stack.stack))
        self.assertEqual(-2, actual_current_min_2)


if __name__ == "__main__":
    unittest.main()
