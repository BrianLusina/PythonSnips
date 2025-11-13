import unittest
from . import reverse_string


class ReverseStringTestCase(unittest.TestCase):
    def test_one(self):
        text = "!evitacudE ot emocleW"
        actual = reverse_string(text)
        expected = "Welcome to Educative!"
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
