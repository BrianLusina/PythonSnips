from pysnips.data_structures import DataStructures
import unittest


class QueueTwoStacksTest(unittest.TestCase):
    def shortDescription(self):
        return "Tests for " + DataStructures.QueueTwoStacks.__name__

    def test_init_queue_two_stacks(self):
        queue = DataStructures.QueueTwoStacks(0)
        self.assertIsInstance(queue, DataStructures.QueueTwoStacks, " Expected an instance of QueueTwoStacks")

    def test_enqueue(self):
        queue = DataStructures.QueueTwoStacks(2)
        queue.enqueue("A")
        queue.enqueue("B")
        self.assertEqual("B", queue.in_stack.peek(), "Expected top stack to be B")

    def test_dequeue(self):
        queue = DataStructures.QueueTwoStacks(4)
        queue.enqueue("A")
        queue.enqueue("B")
        queue.enqueue("C")
        queue.enqueue("D")
        self.assertEqual("A", queue.dequeue(), "Expected top most item from out_stack to be A")

    def test_dequeue_raises_error(self):
        queue = DataStructures.QueueTwoStacks(0)
        with self.assertRaises(IndexError):
            queue.dequeue()
        