from abc import ABC, abstractmethod
from collections import defaultdict
from pprint import PrettyPrinter
from typing import List, Set, Union, Generic, TypeVar
from datastructures.stacks import Stack
from datastructures.graphs.vertex import Vertex
from datastructures.graphs.edge import Edge

T = TypeVar("T")


class Graph(ABC, Generic[T]):
    """
    Represents a Graph Data structure
    """

    def __init__(self, edge_list: List[Edge] = None):
        if edge_list is None:
            edge_list = []
        self.edge_list = edge_list
        self.adjacency_list = defaultdict(List[Vertex])
        self.__construct_adjacency_list()
        self.nodes = []
        self.node_count = len(self.nodes)

    def add(self, source_node: Vertex, destination_node: Vertex):
        """
        Adds a connection between node_one and node_two
        """
        source_node.neighbours.append(destination_node)
        destination_node.neighbours.append(source_node)
        edge = Edge(node_one=source_node, node_two=destination_node)
        self.edge_list.append(edge)
        self.adjacency_list[source_node].append(destination_node)
        self.adjacency_list[destination_node].append(source_node)
        self.nodes.append(source_node)
        self.nodes.append(destination_node)

    def __construct_adjacency_list(self):
        """
        Construct adjacency list
        """
        for edge in self.edge_list:
            self.adjacency_list[edge.node_one].append(edge.node_two)

    @abstractmethod
    def bfs_from_root_to_target(self, root: Vertex, target: Vertex) -> Set[Vertex]:
        """
        Given the root node to traverse and a target node, returns the BFS result of this Graph from the root node to
        the target node
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def bfs_from_node(self, source: Vertex) -> Set[Vertex]:
        """
        Given the source to traverse, returns the BFS result of this Graph from the source node
        """
        raise NotImplementedError("Not yet implemented")

    def topological_sorted_order(self) -> List[Vertex]:
        """
        Returns the topological sorted order of the Graph
        """
        # These static variables are used to perform DFS recursion
        # white nodes depict nodes that have not been visited yet
        # gray nodes depict ongoing recursion
        # black nodes depict recursion is complete
        # An edge leading to a BLACK node is not a "cycle"
        white = 1
        gray = 2
        black = 3

        # Nothing to do here
        if self.node_count == 0:
            return []

        is_possible = True
        stack = Stack()

        # By default all nodes are WHITE
        visited_nodes = {node: white for node in range(self.node_count)}

        def dfs(node: Vertex):
            nonlocal is_possible

            # Don't recurse further if we found a cycle already
            if not is_possible:
                return

            # start recursion
            visited_nodes[node] = gray

            # Traverse on neighbouring nodes/vertices
            if node in self.adjacency_list:
                for neighbour in self.adjacency_list[node]:
                    if visited_nodes[neighbour] == white:
                        dfs(node)
                    elif visited_nodes[node] == gray:
                        # An Edge to a Gray vertex/node represents a cycle
                        is_possible = False

            # Recursion ends. We mark if as BLACK
            visited_nodes[node] = black
            stack.push(node)

        for node in self.nodes:
            # if the node is unprocessed, then call DFS on it
            if visited_nodes[node] == white:
                dfs(node)

        return list(stack.stack) if is_possible else []

    def print(self):
        pretty_print = PrettyPrinter()
        pretty_print.pprint(self.adjacency_list)

    def remove(self, node: Vertex) -> None:
        """
        Removes all references to a node
        :param node
        """
        for _, cxns in self.adjacency_list.items():
            try:
                cxns.remove(node)
            except KeyError:
                pass

        try:
            del self.adjacency_list[node]
        except KeyError:
            pass

    def is_connected(self, node_one: Vertex, node_two: Vertex) -> bool:
        return (
            node_one in self.adjacency_list
            and node_two in self.adjacency_list[node_two]
        )

    def find_path(
        self, node_one: Vertex, node_two: Vertex, path=None
    ) -> Union[List, None]:
        """
        Find any path between node_one and node_two. May not be the shortest path
        :param node_one
        :param node_two
        :param path
        """

        if path is None:
            path = []
        path = [path] + [node_one]

        if node_one.data == node_two.data:
            return path

        if node_one.data not in self.adjacency_list:
            return None

        for node in self.adjacency_list[node_one]:
            if node.data not in path:
                new_path = self.find_path(node, node_two, path)

                if new_path:
                    return new_path

        return None

    def find_all_paths(
        self, node_one: Vertex, node_two: Vertex, path: List = None
    ) -> list:
        """
        Finds all paths between node_one and node_two, where node_one is the start & node_two is the end
        :param node_one Graph Node
        :param node_two Graph Node
        :param path
        """
        if path is None:
            path = []
        path = path + [node_one]

        if node_one.data == node_two.data:
            return [path]

        if node_one.data not in self.adjacency_list:
            return []

        paths = []

        for node in self.adjacency_list[node_one.data]:
            if node not in path:
                newpaths = self.find_all_paths(Vertex(node), node_two, path)
                for newpath in newpaths:
                    paths.append(newpath)

        return paths

    def find_shortest_path(
        self, node_one: Vertex, node_two: Vertex, path: List = None
    ) -> Union[List, None]:
        """
        Finds the shortest path between 2 nodes in the graph
        """
        if path is None:
            path = []

        path = path + [node_one]

        if node_one.data == node_two.data:
            return path

        if node_one.data not in self.adjacency_list:
            return None

        shortest = None

        for node in self.adjacency_list[node_one]:
            if node.data not in path:
                newpath = self.find_shortest_path(node, node_two, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath

        return shortest

    def __str__(self):
        """
        Return string representation of this Graph
        """
        return f"Graph: {self.adjacency_list}"
