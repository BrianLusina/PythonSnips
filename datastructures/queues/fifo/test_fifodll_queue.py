import unittest

from .fifo_with_dll import FifoDllQueue


class FifoDllQueueTestCase(unittest.TestCase):
    def test_1(self):
        fifo_queue = FifoDllQueue()
        fifo_queue.enqueue(1)
        fifo_queue.enqueue(2)
        fifo_queue.enqueue(3)
        fifo_queue.enqueue(4)
        fifo_queue.enqueue(5)

        expected_1 = 1
        actual_data_1 = fifo_queue.dequeue()
        self.assertEqual(expected_1, actual_data_1)

        expected_2 = 2
        actual_data_2 = fifo_queue.dequeue()
        self.assertEqual(expected_2, actual_data_2)

        expected_3 = 3
        actual_data_3 = fifo_queue.dequeue()
        self.assertEqual(expected_3, actual_data_3)

        expected_4 = 4
        actual_data_4 = fifo_queue.dequeue()
        self.assertEqual(expected_4, actual_data_4)

        expected_5 = 5
        actual_data_5 = fifo_queue.dequeue()
        self.assertEqual(expected_5, actual_data_5)

        # at this point, the queue is empty
        actual_data_6 = fifo_queue.dequeue()
        self.assertIsNone(actual_data_6)


if __name__ == '__main__':
    unittest.main()
