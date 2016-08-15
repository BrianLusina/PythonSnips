import unittest
import time


def remove_duplicate(strin):
    return set(strin)


class DuplicateTests(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime

    def test_1(self):
        time.sleep(1)
        self.assertEqual("tre avsl", remove_duplicate("tree traversal"))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DuplicateTests)
    unittest.TextTestRunner(verbosity=0).run(suite)
