import unittest
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.stack.simplify_path import simplify_path

SIMPLIFY_PATH_TEST_CASES = [
    ("/home/", "/home"),
    ("/home//foo/", "/home/foo"),
    ("/home/user/Documents/../Pictures", "/home/user/Pictures"),
    ("/../", "/"),
    ("/.../a/../b/c/../d/./", "/.../b/d"),
]


class SimplifyPathTestCase(unittest.TestCase):
    @parameterized.expand(SIMPLIFY_PATH_TEST_CASES, name_func=custom_test_name_func)
    def test_simplify_path(self, path: str, expected: str):
        actual = simplify_path(path)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
