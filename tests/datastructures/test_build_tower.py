import unittest

from datastructures.lists.build_tower import tower_builder


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(tower_builder(1), ['*', ])

    def test_2(self):
        self.assertEqual(tower_builder(2), [' * ', '***'])

    def test_3(self):
        self.assertEqual(tower_builder(3), ['  *  ', ' *** ', '*****'])

    def test_6(self):
        self.assertEqual(tower_builder(6), ['     *     ',
                                            '    ***    ',
                                            '   *****   ',
                                            '  *******  ',
                                            ' ********* ',
                                            '***********'
                                            ])


if __name__ == '__main__':
    unittest.main()
