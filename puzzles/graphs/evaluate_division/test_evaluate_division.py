import unittest

from . import calc_equation


class EvaluateDivisionTestCase(unittest.TestCase):
    def test_1(self):
        """should return [6.00000,0.50000,-1.00000,1.00000,-1.00000] from equations = [["a","b"],["b","c"]],
        values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]"""
        expected = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        actual = calc_equation(equations, values, queries)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return [3.75000,0.40000,5.00000,0.20000] from equations = [["a","b"],["b","c"],["bc","cd"]],
        values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]"""
        expected = [3.75000, 0.40000, 5.00000, 0.20000]
        equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
        values = [1.5, 2.5, 5.0]
        queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
        actual = calc_equation(equations, values, queries)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return [0.50000,2.00000,-1.00000,-1.00000] from equations = [["a","b"]], values = [0.5],
        queries = [["a","b"],["b","a"],["a","c"],["x","y"]]"""
        expected = [0.50000, 2.00000, -1.00000, -1.00000]
        equations = [["a", "b"]]
        values = [0.5]
        queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
        actual = calc_equation(equations, values, queries)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
