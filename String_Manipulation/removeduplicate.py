import unittest
import time


def remove_duplicate(strin):
    out = ""
    for x in strin:
        if x not in out:
            out += x
    return out


class DuplicateTests(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print("%s: %.3f" % (self.id(), t))

    def test_1(self):
        time.sleep(1)
        self.assertEqual("tre avsl", remove_duplicate("tree traversal"))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DuplicateTests)
    unittest.TextTestRunner(verbosity=0).run(suite)
