import unittest
from . import count_number_of_underpaid_managers, NAryNode


class CountOfUnderpaidManagersTestCase(unittest.TestCase):
    def test_1(self):
        """should return 1 for
                A($100)
                /    \
               /     \
           C(200)       B(120)
           /
        D(60)
        """
        d = NAryNode(60, children=[])
        c = NAryNode(200, children=[d])
        b = NAryNode(120, children=[])
        root_node = NAryNode(100, children=[b, c])
        expected = 1
        actual = count_number_of_underpaid_managers(root_node)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 0 for None root"""
        expected = 0
        actual = count_number_of_underpaid_managers(None)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
