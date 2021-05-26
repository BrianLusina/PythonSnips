import unittest
from random import randint

from bit_manipulation.int32_to_ipv4 import int32_to_ip


class Int32ToIpv4TestCase(unittest.TestCase):
    def test_fixed_tests(self):
        self.assertEqual(int32_to_ip(2154959208), "128.114.17.104")
        self.assertEqual(int32_to_ip(0), "0.0.0.0")
        self.assertEqual(int32_to_ip(2149583361), "128.32.10.1")

    def test_random(self):
        for _ in range(100):
            test_n = randint(0, 2 ** 32 - 1)
            expected = ".".join(
                [str(test_n >> 24 & 0xFF), str(test_n >> 16 & 0xFF), str(test_n >> 8 & 0xFF), str(test_n & 0xFF)])

            self.assertEquals(int32_to_ip(test_n), expected)


if __name__ == '__main__':
    unittest.main()
