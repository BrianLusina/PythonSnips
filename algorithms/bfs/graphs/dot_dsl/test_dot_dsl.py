import unittest

from algorithms.bfs.graphs.dot_dsl import ATTR, EDGE, NODE, Edge, Graph, Node


class DotDslTest(unittest.TestCase):
    def test_empty_graph(self):
        g = Graph()

        self.assertEqual(g.nodes, [])
        self.assertEqual(g.edges, [])
        self.assertEqual(g.attrs, {})

    def test_graph_with_one_node(self):
        g = Graph([(NODE, "a", {})])

        self.assertEqual(g.nodes, [Node("a")])
        self.assertEqual(g.edges, [])
        self.assertEqual(g.attrs, {})

    def test_graph_with_one_node_with_keywords(self):
        g = Graph([(NODE, "a", {"color": "green"})])

        self.assertEqual(g.nodes, [Node("a", {"color": "green"})])
        self.assertEqual(g.edges, [])
        self.assertEqual(g.attrs, {})

    def test_graph_with_one_edge(self):
        g = Graph([(EDGE, "a", "b", {})])

        self.assertEqual(g.nodes, [])
        self.assertEqual(g.edges, [Edge("a", "b", {})])
        self.assertEqual(g.attrs, {})

    def test_graph_with_one_attribute(self):
        g = Graph([(ATTR, "foo", "1")])

        self.assertEqual(g.nodes, [])
        self.assertEqual(g.edges, [])
        self.assertEqual(g.attrs, {"foo": "1"})

    def test_graph_with_attributes(self):
        g = Graph(
            [
                (ATTR, "foo", "1"),
                (ATTR, "title", "Testing Attrs"),
                (NODE, "a", {"color": "green"}),
                (NODE, "c", {}),
                (NODE, "b", {"label", "Beta!"}),
                (EDGE, "b", "c", {}),
                (EDGE, "a", "b", {"color": "blue"}),
                (ATTR, "bar", "true"),
            ]
        )

        self.assertEqual(
            g.nodes,
            [
                Node("a", {"color": "green"}),
                Node("c", {}),
                Node("b", {"label", "Beta!"}),
            ],
        )
        self.assertEqual(
            g.edges, [Edge("b", "c", {}), Edge("a", "b", {"color": "blue"})]
        )
        self.assertEqual(g.attrs, {"foo": "1", "title": "Testing Attrs", "bar": "true"})

    def test_malformed_graph(self):
        with self.assertRaises(TypeError):
            Graph(1)

        with self.assertRaises(TypeError):
            Graph("problematic")

    def test_malformed_graph_item(self):
        with self.assertRaises(TypeError):
            Graph([()])

        with self.assertRaises(TypeError):
            Graph([(ATTR,)])

    def test_malformed_attr(self):
        with self.assertRaises(ValueError):
            Graph([(ATTR, 1, 2, 3)])

    def test_malformed_node(self):
        with self.assertRaises(ValueError):
            Graph([(NODE, 1, 2, 3)])

    def test_malformed_EDGE(self):
        with self.assertRaises(ValueError):
            Graph([(EDGE, 1, 2)])

    def test_unknown_item(self):
        with self.assertRaises(ValueError):
            Graph([(99, 1, 2)])


if __name__ == "__main__":
    unittest.main()
