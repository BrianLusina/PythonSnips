from typing import List, Set

from datastructures.graphs import Edge, Graph, Vertex


class UndirectedGraph(Graph):

    def __init__(self, edge_list: List[Edge]):
        super(UndirectedGraph, self).__init__(edge_list)

    def bfs_from_root_to_target(self, root: Vertex, target: Vertex) -> Set[Vertex]:
        pass

    def bfs_from_node(self, source: Vertex) -> Set[Vertex]:
        pass
