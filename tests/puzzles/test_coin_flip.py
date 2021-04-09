import unittest

from puzzles.coin_flip import coin_flip


class CoinFlipTests(unittest.TestCase):
    def shortDescription(self):
        return "Tests for {}".format(coin_flip.__name__)

    def test_raises_error_on_invalid_inputs(self):
        with self.assertRaises(TypeError):
            coin_flip("5")

    def test_returns_dict(self):
        self.assertIsInstance(coin_flip(5), dict, "Expected dictionary")
