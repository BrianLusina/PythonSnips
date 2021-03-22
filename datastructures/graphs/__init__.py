from abc import ABC, abstractmethod
from collections import defaultdict
from pprint import PrettyPrinter

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
    
    def __str__(self):
        return f"Data: {self.data}"

class Edge(object):
    """
    Edge representation of an Edge in a Graph
    """
    def __init__(self, source: Node = None, destination: Node = None, weight = None):
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

    def __init__(self, connections):
        """
        Initializes a Graph object
        :param connections This is a list/tuple/dict of connections to be created for the Graph. This has been left to the 
        child class to implement
        """
        self.connections = connections
        self._graph = defaultdict(set)
        self.__create_connections()

    def __create_connections(self):
        for a, b in self.connections:
            node_one = Node(data=a)
            node_two = Node(data=b)
            self.add(node_one, node_two)

    @property
    def graph(self):
        pretty_print = PrettyPrinter()
        pretty_print.pprint(self._graph)

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
        for _, cxns in self._graph.items():
            try:
                cxns.remove(node)
            except KeyError:
                pass

        try:
            del self._graph[node]
        except KeyError:
            pass

    def __str__(self):
        """
        Return string representation of this Graph
        """
        return f"{self._graph}"
    
    def is_connected(self, node_one: Node, node_two: Node) -> bool:
        return node_one in self._graph and node_two in self._graph[node_two]

    def find_path(self, node_one: Node, node_two: Node, path: list =[]) -> list:
        """
        Find any path between node_one and node_two. May not be the shortest path
        :param node_one
        :param node_two
        :param path
        """

        path = [path] + [node_one]
        
        if node_one.data == node_two.data:
            return path

        if node_one.data not in self._graph:
            return None
        
        for node in self._graph[node_one]:
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
        
        if node_one.data not in self._graph:
            return []
        
        paths = []
        
        for node in self._graph[node_one.data]:
            if node not in path:
                newpaths = self.find_all_paths(node, node_two, path)
                for newpath in newpaths:
                    paths.append(newpath)

        return paths

    def find_shortest_path(self, node_one: Node, node_two: Node, path: list = []) -> list:
        """
        Finds the shortest path between 2 nodes in the graph
        """
        path = path + [node_one]

        if node_one.data == node_two:
            return path

        if node_one.data not in self._graph:
            return None

        shortest = None

        for node in self._graph[node_one]:
            if node.data not in path:
                newpath = self.find_shortest_path(node, node_two, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath

        return shortest
