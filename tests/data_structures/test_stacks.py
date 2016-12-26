import unittest
from data_structures.stacks import Stack


class StackTestCase(unittest.TestCase):

    def test_stack_initialized(self):
        stack = Stack(0)
        self.assertIsInstance(stack, Stack, "Expected an instance of Stack")

    def test_stack_init_with_max_len(self):
        stack = Stack(10)
        self.assertEqual(10, len(stack), "Expected length of 10")

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

        self.assertEqual(2, stack.get_len(), "Reduce the length of stack after pop")

    def test_stack_push(self):
        stack = Stack(5)
        stack.push("Python")
        stack.push("Java")
        stack.push("JavaScript")
        self.assertEqual("JavaScript", stack.peek(), "Expected last item added to be JavaScript")

if __name__ == '__main__':
    unittest.main()
