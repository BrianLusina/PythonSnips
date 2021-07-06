import unittest

from datastructures.stacks import Stack


class StackTestCase(unittest.TestCase):
    def test_stack_initialized(self):
        stack = Stack(0)
        self.assertIsInstance(stack, Stack, "Expected an instance of Stack")

    def test_empty_stack(self):
        stack = Stack(0)
        self.assertEqual(True, stack.is_empty(), "Expected an empty stack")

    def test_stack_is_full(self):
        stack = Stack(2)
        stack.push("Oranges")
        stack.push("Mangoes")
        self.assertEqual(True, stack.is_full(), "Expected Stack to be full")

    def test_stack_peek(self):
        stack = Stack(2)
        stack.push("Tomatoes")
        stack.push("apples")
        self.assertEqual("apples", stack.peek(), "Expected apples")

    def test_stack_pop(self):
        stack = Stack(3)
        stack.push("Chocolate")
        stack.push("Lollipop")
        stack.push("Nugget")
        self.assertEqual("Nugget", stack.pop(), "Expected Nugget")

        self.assertEqual(2, len(stack), "Reduce the length of stack after pop")

    def test_stack_push(self):
        stack = Stack(5)
        stack.push("Python")
        stack.push("Java")
        stack.push("JavaScript")
        self.assertEqual("JavaScript", stack.peek(), "Expected last item added to be JavaScript")

    def test_push_diff_types(self):
        stack = Stack(5)
        stack.push("Python")
        stack.push(1)
        stack.push(dict(brian="Brian", lusina="Lusina", ombito="Ombito"))
        stack.push((1, 5))
        stack.push(range(5))
        self.assertEqual(range(5), stack.peek(), "Expected last item added to be a range")


if __name__ == '__main__':
    unittest.main()
