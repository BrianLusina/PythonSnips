import unittest
from . import can_visit_all_rooms


class CanVisitAllRoomsTestCase(unittest.TestCase):
    def test_1(self):
        """should return true for rooms=[[1],[2],[3],[]]"""
        rooms = [[1], [2], [3], []]
        actual = can_visit_all_rooms(rooms)
        self.assertTrue(actual)

    def test_2(self):
        """should return False for [[1,3],[3,0,1],[2],[0]]"""
        rooms = [[1, 3], [3, 0, 1], [2], [0]]
        actual = can_visit_all_rooms(rooms)
        self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
