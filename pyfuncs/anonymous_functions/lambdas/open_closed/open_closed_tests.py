import unittest

from Lambdas.OpenClosed.open_closed import greet, spoken, shouted, whispered


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(greet(spoken, "Hello"), "Hello.")

    def test_2(self):
        self.assertEqual(greet(shouted, "Hello"), "HELLO!")

    def test_3(self):
        self.assertEqual(greet(whispered, "Hello"), "hello.")


if __name__ == '__main__':
    unittest.main()
