import unittest
from parameterized import parameterized
from pystrings.lexicographically_largest_string import (
    lexicographically_largest_string_from_box,
    lexicographically_largest_string_from_box_2
)


class LexicographicallyLargestStringFromBoxTestCase(unittest.TestCase):
    @parameterized.expand(
        [
            ("acbd", 2, "d"),
            ("zzzzz", 5, "z"),
            ("aazz", 1, "aazz"),
            ("yxa", 2, "yx"),
            ("dbca", 2, "dbc"),
            ("gggg", 4, "g"),
            ("zxya", 3, "zx"),
            ("mnopqr", 3, "r"),
            (
                "ajhpnonbogfhxanqumtrgosqwjubctnwxcjxgvophccygoomigxlkhsxnnitsyqkiwmrrlekphwpgtsvjsbokakzpdkdzzdnbgmaepkhuohdlvzsfiokivnhybybinedxbkgdpjdktxkezfyvcxegobkfdnmdiupsfjsobwpseucjbzkvqoqxbnsoqjlldqjpjqkjvzdmpnyrwtkbezhmrsdzfgsjmycaydczpiotkvjzwcoiihunqmzylccuekkdebhgiifwrlbramdqsbwzbuoyluqqtdaroa",
                1,
                "ajhpnonbogfhxanqumtrgosqwjubctnwxcjxgvophccygoomigxlkhsxnnitsyqkiwmrrlekphwpgtsvjsbokakzpdkdzzdnbgmaepkhuohdlvzsfiokivnhybybinedxbkgdpjdktxkezfyvcxegobkfdnmdiupsfjsobwpseucjbzkvqoqxbnsoqjlldqjpjqkjvzdmpnyrwtkbezhmrsdzfgsjmycaydczpiotkvjzwcoiihunqmzylccuekkdebhgiifwrlbramdqsbwzbuoyluqqtdaroa",
            ),
        ]
    )
    def test_lexicographically_largest_string_from_box(
        self, word: str, num: int, expected: str
    ):
        actual = lexicographically_largest_string_from_box(word, num)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            ("acbd", 2, "d"),
            ("zzzzz", 5, "z"),
            ("aazz", 1, "aazz"),
            ("yxa", 2, "yx"),
            ("dbca", 2, "dbc"),
            ("gggg", 4, "g"),
            ("zxya", 3, "zx"),
            ("mnopqr", 3, "r"),
            (
                "ajhpnonbogfhxanqumtrgosqwjubctnwxcjxgvophccygoomigxlkhsxnnitsyqkiwmrrlekphwpgtsvjsbokakzpdkdzzdnbgmaepkhuohdlvzsfiokivnhybybinedxbkgdpjdktxkezfyvcxegobkfdnmdiupsfjsobwpseucjbzkvqoqxbnsoqjlldqjpjqkjvzdmpnyrwtkbezhmrsdzfgsjmycaydczpiotkvjzwcoiihunqmzylccuekkdebhgiifwrlbramdqsbwzbuoyluqqtdaroa",
                1,
                "ajhpnonbogfhxanqumtrgosqwjubctnwxcjxgvophccygoomigxlkhsxnnitsyqkiwmrrlekphwpgtsvjsbokakzpdkdzzdnbgmaepkhuohdlvzsfiokivnhybybinedxbkgdpjdktxkezfyvcxegobkfdnmdiupsfjsobwpseucjbzkvqoqxbnsoqjlldqjpjqkjvzdmpnyrwtkbezhmrsdzfgsjmycaydczpiotkvjzwcoiihunqmzylccuekkdebhgiifwrlbramdqsbwzbuoyluqqtdaroa",
            ),
        ]
    )
    def test_lexicographically_largest_string_from_box_2(
        self, word: str, num: int, expected: str
    ):
        actual = lexicographically_largest_string_from_box_2(word, num)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
