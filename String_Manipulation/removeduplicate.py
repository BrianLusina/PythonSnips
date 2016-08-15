import unittest
import time


class RemoveDuplicate(object):
    """
    loop through characters in string and check if it is not in output string
    if not, add to output string, return the string.
    """
    def __init__(self, strin):
        self.strin = strin

    def remove_duplicate(self):
        out = ""
        for x in self.strin.lower():
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
        rem = RemoveDuplicate("tree traversal")
        self.assertEqual("tre avsl", rem.remove_duplicate())

    def test_2(self):
        time.sleep(2)
        rem = RemoveDuplicate("Duplicate duplicate")
        self.assertEqual("duplicate ", rem.remove_duplicate())


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DuplicateTests)
    unittest.TextTestRunner(verbosity=0).run(suite)
