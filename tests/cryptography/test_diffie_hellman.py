import unittest

from cryptography.diffie_hellman import private_key, secret, public_key


class DiffieHellmanTest(unittest.TestCase):

    def test_private_key_is_in_range(self):
        primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        for i in primes:
            self.assertTrue(1 < private_key(i) < i)

    # Can fail due to randomness, but most likely will not,
    # due to pseudo-randomness and the large number chosen
    def test_private_key_is_random(self):
        p = 2147483647
        private_keys = []
        for i in range(5):
            private_keys.append(private_key(p))
        self.assertEqual(len(set(private_keys)), len(private_keys))

    def test_can_calculate_public_key_using_private_key(self):
        p = 23
        g = 5
        private = 6
        expected = 8

        actual = public_key(p, g, private)
        self.assertEqual(actual, expected)

    def test_can_calculate_secret_using_other_party_s_public_key(self):
        p = 23
        public = 19
        private = 6
        expected = 2

        actual = secret(p, public, private)
        self.assertEqual(actual, expected)

    def test_key_exchange(self):
        p = 23
        g = 5
        alice_private_key = private_key(p)
        bob_private_key = private_key(p)
        alice_public_key = public_key(p, g, alice_private_key)
        bob_public_key = public_key(p, g, bob_private_key)
        secret_a = secret(p, bob_public_key, alice_private_key)
        secret_b = secret(p, alice_public_key, bob_private_key)

        self.assertEqual(secret_a, secret_b)


if __name__ == '__main__':
    unittest.main()
