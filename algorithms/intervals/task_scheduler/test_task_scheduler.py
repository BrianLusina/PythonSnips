import unittest
from typing import List
from parameterized import parameterized
from algorithms.intervals.task_scheduler import (
    least_intervals_mathematical,
    least_intervals_with_max_heap,
)


class LeastIntervalsTestCase(unittest.TestCase):
    @parameterized.expand(
        [
            (["A", "A", "B", "B"], 2, 5),
            (["A", "B", "A", "A", "B", "C"], 3, 9),
            (["A", "C", "B", "A"], 0, 4),
            (["A", "A", "A", "B", "B", "C", "C"], 1, 7),
            (["S", "I", "V", "U", "W", "D", "U", "X"], 0, 8),
            (
                [
                    "A",
                    "K",
                    "X",
                    "M",
                    "W",
                    "D",
                    "X",
                    "B",
                    "D",
                    "C",
                    "O",
                    "Z",
                    "D",
                    "E",
                    "Q",
                ],
                3,
                15,
            ),
            (
                [
                    "A",
                    "B",
                    "C",
                    "O",
                    "Q",
                    "C",
                    "Z",
                    "O",
                    "X",
                    "C",
                    "W",
                    "Q",
                    "Z",
                    "B",
                    "M",
                    "N",
                    "R",
                    "L",
                    "C",
                    "J",
                ],
                10,
                34,
            ),
        ]
    )
    def test_least_intervals_mathematical(
        self, tasks: List[str], n: int, expected: int
    ):
        actual = least_intervals_mathematical(tasks, n)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            (["A", "A", "B", "B"], 2, 5),
            (["A", "B", "A", "A", "B", "C"], 3, 9),
            (["A", "C", "B", "A"], 0, 4),
            (["A", "A", "A", "B", "B", "C", "C"], 1, 7),
            (["S", "I", "V", "U", "W", "D", "U", "X"], 0, 8),
            (
                [
                    "A",
                    "K",
                    "X",
                    "M",
                    "W",
                    "D",
                    "X",
                    "B",
                    "D",
                    "C",
                    "O",
                    "Z",
                    "D",
                    "E",
                    "Q",
                ],
                3,
                15,
            ),
            (
                [
                    "A",
                    "B",
                    "C",
                    "O",
                    "Q",
                    "C",
                    "Z",
                    "O",
                    "X",
                    "C",
                    "W",
                    "Q",
                    "Z",
                    "B",
                    "M",
                    "N",
                    "R",
                    "L",
                    "C",
                    "J",
                ],
                10,
                34,
            ),
        ]
    )
    def test_least_intervals_max_heap(self, tasks: List[str], n: int, expected: int):
        actual = least_intervals_with_max_heap(tasks, n)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
