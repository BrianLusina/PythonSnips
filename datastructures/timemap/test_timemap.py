import unittest

from . import TimeMap


class TimeMapTestCase(unittest.TestCase):
    def test_1(self):
        """set('foo', 'bar', 1) -> get('foo', 1) -> get('foo', 3) -> get('foo', 3) -> set('foo', 'bar2', 4) -> get('foo', 4) -> get('foo', 5)"""
        time_map = TimeMap()

        # store the key "foo" and value "bar" along with timestamp = 1.
        time_map.set("foo", "bar", 1)

        # return "bar"
        expected_bar = "bar"
        actual_at_time_1 = time_map.get("foo", 1)
        self.assertEqual(expected_bar, actual_at_time_1)

        # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value
        # is at timestamp 1 is "bar".
        expected_bar_2 = "bar"
        actual_at_time_3 = time_map.get("foo", 3)
        self.assertEqual(expected_bar_2, actual_at_time_3)

        # store the key "foo" and value "bar2" along with timestamp = 4.
        time_map.set("foo", "bar2", 4)

        # return "bar2"
        expected_bar_2_2 = "bar2"
        actual_at_time_4 = time_map.get("foo", 4)
        self.assertEqual(expected_bar_2_2, actual_at_time_4)

        # return "bar2"
        expected_bar_2_3 = "bar2"
        actual_at_time_5 = time_map.get("foo", 5)
        self.assertEqual(expected_bar_2_3, actual_at_time_5)


if __name__ == "__main__":
    unittest.main()
