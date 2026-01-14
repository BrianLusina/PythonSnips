import unittest
from typing import List
from parameterized import parameterized
from algorithms.heap.schedule_tasks import minimum_machines

SCHEDULE_TASKS_ON_MINIMUM_MACHINES = [
    ([[1, 7], [8, 13], [5, 6], [10, 14], [6, 7]], 2),
    ([[1, 7], [8, 9], [3, 6], [9, 14], [6, 7]], 2),
    ([[2, 5], [2, 5], [2, 5], [2, 5]], 4),
    ([[2, 3], [4, 7], [8, 18], [19, 25], [26, 30]], 1),
    ([[12, 13], [13, 15], [17, 20], [13, 14], [19, 21], [18, 20]], 3),
    ([[1, 4], [3, 5], [6, 8], [7, 8]], 2),
    ([[1, 7], [1, 7], [1, 7], [1, 7], [1, 7], [1, 7]], 6),
    ([[1, 3], [3, 5], [5, 9], [9, 12], [12, 13], [13, 16], [16, 17]], 1),
    ([[1, 3], [2, 6], [5, 9], [4, 7], [8, 10], [8, 10], [12, 15]], 3),
    ([[5, 6], [5, 6], [5, 6], [5, 6], [6, 7]], 4),
    ([[5, 6], [6, 7], [1, 7], [10, 14], [8, 13]], 2),
]


class ScheduleTasksOnMinimumMachinesTestCase(unittest.TestCase):
    @parameterized.expand(SCHEDULE_TASKS_ON_MINIMUM_MACHINES)
    def test_schedule_tasks_on_minimum_machines(
        self, tasks: List[List[int]], expected: int
    ):
        actual = minimum_machines(tasks)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
