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
        self._graph[node_one.data].add(node_two.data)

    def contains_cycle(self) -> bool:
        """
        Checks if this graph contains a cycle
        :returns bool True if it contains a cycle, False otherwise
        """
        visited = set()
        path = [object()]
        path_set = set(path)
        stack = [iter(self._graph)]

        while stack:
            for node in stack[-1]:
                if node in path_set:
                    return True

                elif node not in visited:
                    visited.add(node)

                    path.append(node)

                    path_set.add(node)
                    
                    stack.append(iter(self._graph.get(node, set())))

                    break
            else:
                path_set.remove(path.pop())
                stack.pop()
        return False
    