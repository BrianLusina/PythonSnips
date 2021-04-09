import time
import unittest

from pystrings.remove_duplicate import RemoveDuplicate, RemoveDupSort


class DuplicateTests(unittest.TestCase):
    def setUp(self):
        self.start_time = time.time()

    def tearDown(self):
        t = time.time() - self.start_time
        print("%s: %.3f" % (self.id(), t))

    def test_1(self):
        time.sleep(1)
        rem = RemoveDuplicate("tree traversal")
        self.assertEqual("tre avsl", rem.remove_duplicate())

    def test_2(self):
        time.sleep(2)
        rem = RemoveDuplicate("Duplicate duplicate")
        self.assertEqual("duplicate ", rem.remove_duplicate())

    def test_3(self):
        time.sleep(3)
        rem = RemoveDuplicate("end game")
        self.assertEqual("end gam", rem.remove_duplicate())

    def test_4(self):
        time.sleep(4)
        rem = RemoveDuplicate("me and you and them and me")
        self.assertEqual("me andyouth", rem.remove_duplicate())

    def test_5(self):
        time.sleep(5)
        sent = RemoveDupSort("hello world and practice makes perfect and hello world again")
        self.assertEqual("again and hello makes perfect practice world", sent.remover())


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DuplicateTests)
    unittest.TextTestRunner(verbosity=0).run(suite)
