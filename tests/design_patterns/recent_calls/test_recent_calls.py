import unittest

from design_patterns.recent_counter import RecentCounter


class RecentCounterTest(unittest.TestCase):

    def test_3_calls(self):
        recent_counter = RecentCounter()

        actual_ping_1 = recent_counter.ping(1)
        self.assertEquals(actual_ping_1, 1)

        actual_ping_100 = recent_counter.ping(100)
        self.assertEquals(actual_ping_100, 2)

        actual_ping_3001 = recent_counter.ping(3001)
        self.assertEquals(actual_ping_3001, 3)

        actual_ping_3002 = recent_counter.ping(3002)
        self.assertEquals(actual_ping_3002, 3)


if __name__ == '__main__':
    unittest.main()
