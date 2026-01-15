import unittest
from . import connect_sticks, connect_sticks_2


class MinCostConnectSticksTestCase(unittest.TestCase):
    def test_1(self):
        sticks = [3, 5, 4]
        expected = 19
        actual = connect_sticks(sticks)
        self.assertEqual(expected, actual)

    def test_2(self):
        sticks = [2, 9, 4, 6]
        expected = 39
        actual = connect_sticks(sticks)
        self.assertEqual(expected, actual)

    def test_3(self):
        sticks = [23]
        expected = 0
        actual = connect_sticks(sticks)
        self.assertEqual(expected, actual)

    def test_4(self):
        sticks = [3, 3, 3]
        expected = 15
        actual = connect_sticks(sticks)
        self.assertEqual(expected, actual)

    def test_5(self):
        sticks = [1, 10, 3, 3, 3]
        expected = 40
        actual = connect_sticks(sticks)
        self.assertEqual(expected, actual)

    def test_6(self):
        sticks = [7, 10, 16]
        expected = 50
        actual = connect_sticks(sticks)
        self.assertEqual(expected, actual)

    def test_7(self):
        sticks = [5, 120, 7, 30, 10]
        expected = 258
        actual = connect_sticks(sticks)
        self.assertEqual(expected, actual)

    def test_8(self):
        sticks = [100, 200, 300, 400, 500]
        expected = 3300
        actual = connect_sticks(sticks)
        self.assertEqual(expected, actual)

    def test_9(self):
        sticks = [20, 20, 20, 20]
        expected = 160
        actual = connect_sticks(sticks)
        self.assertEqual(expected, actual)


class MinCostConnectSticks2TestCase(unittest.TestCase):
    def test_1(self):
        sticks = [3, 5, 4]
        expected = 19
        actual = connect_sticks_2(sticks)
        self.assertEqual(expected, actual)

    def test_2(self):
        sticks = [2, 9, 4, 6]
        expected = 39
        actual = connect_sticks_2(sticks)
        self.assertEqual(expected, actual)

    def test_3(self):
        sticks = [23]
        expected = 0
        actual = connect_sticks_2(sticks)
        self.assertEqual(expected, actual)

    def test_4(self):
        sticks = [3, 3, 3]
        expected = 15
        actual = connect_sticks_2(sticks)
        self.assertEqual(expected, actual)

    def test_5(self):
        sticks = [1, 10, 3, 3, 3]
        expected = 40
        actual = connect_sticks_2(sticks)
        self.assertEqual(expected, actual)

    def test_6(self):
        sticks = [7, 10, 16]
        expected = 50
        actual = connect_sticks_2(sticks)
        self.assertEqual(expected, actual)

    def test_7(self):
        sticks = [5, 120, 7, 30, 10]
        expected = 258
        actual = connect_sticks_2(sticks)
        self.assertEqual(expected, actual)

    def test_8(self):
        sticks = [100, 200, 300, 400, 500]
        expected = 3300
        actual = connect_sticks_2(sticks)
        self.assertEqual(expected, actual)

    def test_9(self):
        sticks = [20, 20, 20, 20]
        expected = 160
        actual = connect_sticks_2(sticks)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
