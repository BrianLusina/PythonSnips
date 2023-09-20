import unittest
from . import SnapshotArray


class SnapshotTestCase(unittest.TestCase):
    def test_1(self):
        """set(3) -> snap(0, 5) -> set(0, 6) -> get(0, 0)"""
        snapshot_array = SnapshotArray(3)
        snapshot_array.set(0, 5)

        expected_first_snap = 0
        actual_first_snap = snapshot_array.snap()

        self.assertEqual(expected_first_snap, actual_first_snap)

        snapshot_array.set(0, 6)

        expected_first_snap_id = 5
        actual_first_snap_id = snapshot_array.get(0, 0)

        self.assertEqual(expected_first_snap_id, actual_first_snap_id)


if __name__ == '__main__':
    unittest.main()
