from datastructures.graphs import Graph, Node
from typing import List, Tuple


class UnDirectedGraph(Graph):

    def __init__(self, edge_list: List[Tuple[Node, Node]]):
        super(UnDirectedGraph, self).__init__(edge_list)

    def add(self, node_one: Node, node_two: Node) -> None:
        """
        Adds connections/edges between Node 1 and Node 2.
        Since this is an undirected Graph. Connection will be from Node 1 to Node 2 and from node 2 to node 1
        """
        node_one.next = node_two
        self.adjacency_list.append((node_one, node_two))
