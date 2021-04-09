import unittest

from pystrings.string_destroyer import destroyer


class MyTestCase(unittest.TestCase):

    def shortDescription(self):
        return "Test String destroyer"

    def test_1(self):
        input_sets = ({'A', 'b'}, {'C', 'd'})
        self.assertEqual(destroyer(input_sets), "a _ c _ e f g h i j k l m n o p q r s t u v w x y z")

    def test_2(self):
        input_sets = ({'b', 'b'}, {'C', 'm', 'f'})
        self.assertEqual(destroyer(input_sets), "a _ c d e _ g h i j k l _ n o p q r s t u v w x y z")


if __name__ == '__main__':
    unittest.main()
