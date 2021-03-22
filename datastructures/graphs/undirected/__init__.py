from pysnips.data_structures.graphs import Graph, Node, Edge
from collections import defaultdict
from pprint import pprint, PrettyPrinter

class UnDirectedGraph(Graph):

    def __init__(self, connections):
        super().__init__(connections)

    def add(self, node_one, node_two) -> None:
        """
        Adds connections/edges between Node 1 and Node 2.
        Since this is an undirected Graph. Connection will be from Node 1 to Node 2 and from node 2 to node 1
        """
        self._graph[node_one].add(node_two)
        self._graph[node_two].add(node_one)
    


    