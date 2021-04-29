from typing import List

from .. import Graph, Edge


class DirectedGraph(Graph):

    def __init__(self, edge_list: List[Edge]):
        super(DirectedGraph, self).__init__(edge_list)

    def contains_cycle(self) -> bool:
        """
        Checks if this graph contains a cycle
        :returns bool True if it contains a cycle, False otherwise
        """
        visited = set()
        path = [object()]
        path_set = set(path)
        stack = [iter(self.adjacency_list)]

        while stack:
            for node in stack[-1]:
                if node in path_set:
                    return True

                elif node not in visited:
                    visited.add(node)

                    path.append(node)

                    path_set.add(node)

                    stack.append(iter(self.adjacency_list.get(node, set())))

                    break
            else:
                path_set.remove(path.pop())
                stack.pop()
        return False
