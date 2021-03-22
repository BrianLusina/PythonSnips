from .. import Graph, Node, Edge
from collections import defaultdict
from pprint import pprint, PrettyPrinter

class DirectedGraph(Graph):

    def __init__(self, connections):
        super().__init__(connections)

    def add(self, node_one: Node, node_two: Node) -> None:
        """
        Adds connections/edges between Node 1 and Node 2.
        Since this is a Directed Graph. Connection will be from Node 1 to Node 2
        """
        self._graph[node_one.data].add(node_two)
    