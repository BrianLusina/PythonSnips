import time
import unittest

from cryptography.shell_game import ShellGame


class ShellGameTests(unittest.TestCase):
    def setUp(self):
        self.start_time = time.time()

    def tearDown(self):
        t = self.start_time - time.time()
        print("%s: %.3f" % (self.id(), t))

    def test_1(self):
        time.sleep(1)
        shell = ShellGame(5, [])
        self.assertEqual(5, shell.find_the_ball(), "An Empty swap does nothin")

    def test_2(self):
        time.sleep(2)
        shell = ShellGame(0, [(0, 1), (2, 1), (0, 1)])
        self.assertEqual(1, shell.find_the_ball(), "Find the ball in position 2")

    def test_3(self):
        time.sleep(3)
        shell = ShellGame(4, [[0, 9], [9, 3], [3, 7], [7, 8], [8, 2], [4, 5]])
        self.assertEqual(5, shell.find_the_ball(), "Nope! Expected 5.")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ShellGameTests)
    unittest.TextTestRunner(verbosity=0).run(suite)
