import unittest
from . import StreamChecker


class StreamCheckerTestCase(unittest.TestCase):
    def test_1(self):
        words = ["go", "hi"]
        stream = StreamChecker(words)
        self.assertFalse(stream.query("h"))
        self.assertTrue(stream.query("i"))
        self.assertFalse(stream.query("g"))
        self.assertTrue(stream.query("o"))
        self.assertFalse(stream.query("x"))
        self.assertFalse(stream.query("y"))

    def test_2(self):
        words = ["no", "yes"]
        stream = StreamChecker(words)
        self.assertFalse(stream.query("y"))
        self.assertFalse(stream.query("e"))
        self.assertTrue(stream.query("s"))
        self.assertFalse(stream.query("n"))
        self.assertTrue(stream.query("o"))

    def test_3(self):
        words = ["a", "aa"]
        stream = StreamChecker(words)
        self.assertTrue(stream.query("a"))
        self.assertTrue(stream.query("a"))
        self.assertTrue(stream.query("a"))
        self.assertFalse(stream.query("b"))


if __name__ == '__main__':
    unittest.main()
