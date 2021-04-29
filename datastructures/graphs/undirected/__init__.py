from typing import List

from datastructures.graphs import Graph, Edge


class UnDirectedGraph(Graph):

    def __init__(self, edge_list: List[Edge]):
        super(UnDirectedGraph, self).__init__(edge_list)
