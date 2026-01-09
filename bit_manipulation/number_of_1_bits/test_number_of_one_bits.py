import unittest
from parameterized import parameterized
from bit_manipulation.number_of_1_bits import count_bits

NUMBER_OF_ONE_BITS_TEST_CASES = [
    ("unsigned integer 3", 0b00000000000000000000000000000011, 2),
    ("unsigned integer 25", 0b00000000000000000000000000011001, 3),
    ("unsigned integer 725", 0b00000000000000000000001011010101, 6),
    ("unsigned integer 2500", 0b00000000000000000000100111000100, 5),
    ("unsigned integer 3253", 0b00000000000000000000110010110101, 7),
    ("unsigned integer 2147483647", 0b01111111111111111111111111111111, 31),
]


class NumberOfOneBitsTestCase(unittest.TestCase):
    @parameterized.expand(NUMBER_OF_ONE_BITS_TEST_CASES)
    def test_count_bits(self, _, n: int, expected: int):
        actual = count_bits(n)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
