import unittest
import time

class ShellGame(object):
    def __init__(self, start, swaps):
        self.start = start
        self.swaps = swaps

    def find_the_ball(self):


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
        shell = ShellGame(0,[(0, 1), (2, 1), (0, 1)])
        self.assertEqual(2, shell.find_the_ball(),"Find the ball in position 2")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ShellGameTests)
    unittest.TextTestRunner(verbosity=0).run(suite)
