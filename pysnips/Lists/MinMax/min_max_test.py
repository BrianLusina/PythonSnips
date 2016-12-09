import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(min_max(lst), res, "tested on " + str(lst))


if __name__ == '__main__':
    unittest.main()
