from unittest import TestCase, main

from pymath.cyclic_primes import find_number_of_cyclic_primes


class CyclicPrimesTest(TestCase):

    def test_up_to_limit_100(self):
        self.assertEqual(find_number_of_cyclic_primes(2, 100), 13)

    def test_up_to_limit_1_000_000(self):
        self.assertEqual(find_number_of_cyclic_primes(2, 1_000_000), 55)


if __name__ == "__main__":
    main()
