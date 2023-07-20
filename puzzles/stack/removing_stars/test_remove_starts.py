import unittest

from utils.context_mgrs.perf_timer import timing
from . import remove_stars_with_stack


class RemoveStartsTestCase(unittest.TestCase):
    def test_one(self):
        """should return lecoe from leet**cod*e"""
        word = "leet**cod*e"
        expected = "lecoe"

        with timing(f"{word}") as timed:
            actual = remove_stars_with_stack(word)

        self.assertEqual(expected, actual)
        print(f"Execution of remove_stars_with_stack(%s) took %.6f s" % timed())

    def test_two(self):
        """should return '' from erase*****"""
        word = "erase*****"
        expected = ""

        with timing(f"{word}") as timed:
            actual = remove_stars_with_stack(word)

        self.assertEqual(expected, actual)
        print(f"Execution of remove_stars_with_stack(%s) took %.6f s" % timed())


if __name__ == '__main__':
    unittest.main()
