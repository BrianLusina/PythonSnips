import unittest

from datastructures.graphs import Vertex, UndirectedEdge


class VertexTestCases(unittest.TestCase):
    def test_1(self):
        node_one = Vertex(data=1)
        node_two = Vertex(data=2)
        edge = UndirectedEdge(node_one=node_one, node_two=node_two)

        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
