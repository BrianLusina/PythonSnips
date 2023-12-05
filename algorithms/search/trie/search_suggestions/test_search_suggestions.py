import unittest
from . import suggested_products


class SuggestedProductsTestCase(unittest.TestCase):
    def test_1(self):
        """products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"""
        products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
        search_word = "mouse"
        expected = [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mouse", "mousepad"],
                    ["mouse", "mousepad"], ["mouse", "mousepad"]]
        actual = suggested_products(products, search_word)
        self.assertEqual(expected, actual)

    def test_2(self):
        """products = ["havana"], searchWord = "havana"""
        products = ["havana"]
        search_word = "havana"
        expected = [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]]
        actual = suggested_products(products, search_word)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
