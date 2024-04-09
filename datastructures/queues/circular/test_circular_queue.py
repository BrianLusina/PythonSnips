import unittest

from . import CircularQueue, CircularLinkedListQueue
from ..exceptions import QueueEmptyException


class CircularQueueTestCase(unittest.TestCase):
    def test_1(self):
        circular_queue = CircularQueue(5)
        circular_queue.enqueue(1)
        circular_queue.enqueue(2)
        circular_queue.enqueue(3)
        circular_queue.enqueue(4)
        circular_queue.enqueue(5)

        expected_1 = 1
        actual_data_1 = circular_queue.dequeue()
        self.assertEqual(expected_1, actual_data_1)

        expected_2 = 2
        actual_data_2 = circular_queue.dequeue()
        self.assertEqual(expected_2, actual_data_2)

        expected_3 = 3
        actual_data_3 = circular_queue.dequeue()
        self.assertEqual(expected_3, actual_data_3)

        expected_4 = 4
        actual_data_4 = circular_queue.dequeue()
        self.assertEqual(expected_4, actual_data_4)

        expected_5 = 5
        actual_data_5 = circular_queue.dequeue()
        self.assertEqual(expected_5, actual_data_5)

        # at this point, the queue is empty
        with self.assertRaises(QueueEmptyException):
            circular_queue.dequeue()

    def test_2_circular_linked_list_queue(self):
        circular_linked_list_queue = CircularLinkedListQueue(5)
        circular_linked_list_queue.enqueue(1)
        circular_linked_list_queue.enqueue(2)
        circular_linked_list_queue.enqueue(3)
        circular_linked_list_queue.enqueue(4)
        circular_linked_list_queue.enqueue(5)

        expected_1 = 1
        actual_data_1 = circular_linked_list_queue.dequeue()
        self.assertEqual(expected_1, actual_data_1)

        expected_2 = 2
        actual_data_2 = circular_linked_list_queue.dequeue()
        self.assertEqual(expected_2, actual_data_2)

        expected_3 = 3
        actual_data_3 = circular_linked_list_queue.dequeue()
        self.assertEqual(expected_3, actual_data_3)

        expected_4 = 4
        actual_data_4 = circular_linked_list_queue.dequeue()
        self.assertEqual(expected_4, actual_data_4)

        expected_5 = 5
        actual_data_5 = circular_linked_list_queue.dequeue()
        self.assertEqual(expected_5, actual_data_5)

        # at this point, the queue is empty
        with self.assertRaises(QueueEmptyException):
            circular_linked_list_queue.dequeue()


if __name__ == "__main__":
    unittest.main()
