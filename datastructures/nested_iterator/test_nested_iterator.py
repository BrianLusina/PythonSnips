import unittest
from typing import List
from parameterized import parameterized
from datastructures.nested_iterator import (
    NestedIterator,
    NestedInteger,
    NestedIteratorV2,
)
from utils.test_utils import custom_test_name_func


NESTED_ITERATOR_TEST_CASES = [
    ([1, [2, 3], 4], [1, 2, 3, 4]),
    ([3, [2, 3, 4], 4, [2, 3]], [3, 2, 3, 4, 4, 2, 3]),
    ([[2, 3], 3, [2, 3], 4, [2, 3, 4, 5]], [2, 3, 3, 2, 3, 4, 2, 3, 4, 5]),
    ([1, [3, [4, [5, 6], 7], 8], 9], [1, 3, 4, 5, 6, 7, 8, 9]),
    ([[2, 3, [2, 3]]], [2, 3, 2, 3]),
]


def create_nested_iterator_structure(input_list):
    def parse_input(nested, input_list):
        if isinstance(input_list, int):
            nested.set_integer(input_list)
        else:
            for item in input_list:
                child = NestedInteger()
                nested.add(child)
                parse_input(child, item)

    nested_structure = NestedInteger()
    parse_input(nested_structure, input_list)
    return nested_structure


def create_nested_iterator_from_structure(nested_structure):
    return NestedIterator(nested_structure.get_list())


def create_nested_iterator_v2_from_structure(nested_structure):
    return NestedIteratorV2(nested_structure.get_list())


def flatten_list(nested_iterator_object):
    result = []
    while nested_iterator_object.has_next():
        result.append(nested_iterator_object.next())
    return result


class NestedIteratorTestCase(unittest.TestCase):
    @parameterized.expand(NESTED_ITERATOR_TEST_CASES, name_func=custom_test_name_func)
    def test_nested_iterator_dfs(
        self, nested_list: List[List[int]], expected: List[int]
    ):
        nested_integer = create_nested_iterator_structure(nested_list)
        nested_iterator = create_nested_iterator_from_structure(nested_integer)
        actual = flatten_list(nested_iterator)
        self.assertEqual(expected, actual)

    @parameterized.expand(NESTED_ITERATOR_TEST_CASES, name_func=custom_test_name_func)
    def test_nested_iterator_stack(
        self, nested_list: List[List[int]], expected: List[int]
    ):
        nested_integer = create_nested_iterator_structure(nested_list)
        nested_iterator = create_nested_iterator_v2_from_structure(nested_integer)
        actual = flatten_list(nested_iterator)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
