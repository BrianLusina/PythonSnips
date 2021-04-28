from abc import ABC, abstractmethod
from collections import defaultdict
from pprint import PrettyPrinter
from typing import List, Tuple


class Node(object):
    """
    Graph Node representing a Node in a Graph
    """

    def __init__(self, data):
        """
        Initializes a Node object
        :param data Value/data stored within this node
        """
        self.data = data
        self.next = None
        self.neighbours = defaultdict(list)

    def __str__(self):
        return f"Data: {self.data}"


class Edge(object):
    """
    Edge representation of an Edge in a Graph
    """

    def __init__(self, source: Node = None, destination: Node = None, weight=None):
        """
        Initializes an Edge object
        :param source Source Node
        :param destination Destination node
        :param weight This is useful for graphs whose edges are weighted
        """
        self.source = source
        self.destination = destination
        self.weight = weight


class Graph(ABC):
    """
    Represents a Graph Data structure
    """

    def __init__(self, edge_list: List[Tuple[Node, Node]] = None):
        """
        Initializes a Graph object by passing in an adjacency list
        :param edge_list list of edges with all the Nodes of the graph
        """
        if edge_list is None:
            edge_list = []
        self.adjacency_list = edge_list

    @property
    def graph(self):
        pretty_print = PrettyPrinter()
        pretty_print.pprint(self.adjacency_list)

    @abstractmethod
    def add(self, node_one: Node, node_two: Node):
        """
        Adds a connection between node_one and node_two
        """
        raise NotImplementedError("Method has not been implemented")

    def remove(self, node: Node) -> None:
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

    def __str__(self):
        """
        Return string representation of this Graph
        """
        return f"Graph: {self.adjacency_list}"

    def is_connected(self, node_one: Node, node_two: Node) -> bool:
        return node_one in self.adjacency_list and node_two in self.adjacency_list[node_two]

    def find_path(self, node_one: Node, node_two: Node, path=None) -> list:
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

    def find_all_paths(self, node_one: Node, node_two: Node, path: list = []) -> list:
        """
        Finds all paths between node_one and node_two, where node_one is the start & node_two is the end
        :param node_one Graph Node 
        :param node_two Graph Node 
        :param path
        """
        path = path + [node_one]

        if node_one.data == node_two.data:
            return [path]

        if node_one.data not in self.adjacency_list:
            return []

        paths = []

        for node in self.adjacency_list[node_one.data]:
            if node not in path:
                newpaths = self.find_all_paths(Node(node), node_two, path)
                for newpath in newpaths:
                    paths.append(newpath)

        return paths

    def find_shortest_path(self, node_one: Node, node_two: Node, path: list = []) -> list:
        """
        Finds the shortest path between 2 nodes in the graph
        """
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
