from typing import List, Set

from datastructures.queues.fifo import FifoQueue as Queue
from .. import Graph, Edge, Vertex


class DirectedGraph(Graph):

    def __init__(self, edge_list: List[Edge]):
        super(DirectedGraph, self).__init__(edge_list)

    def bfs_from_root_to_target(self, root: Vertex, target: Vertex) -> Set[Vertex]:
        # store all nodes awaiting processing
        queue = Queue()
        # marks visited nodes
        visited = set()

        # add root to queue
        queue.enqueue(root)
        visited.add(root)

        while not queue.is_empty():
            current = queue.dequeue()

            if current == target:
                return visited

            for next_node in current.neighbours:
                if next_node not in visited:
                    queue.enqueue(next_node)
                    visited.add(next_node)

        return visited

    def bfs_from_node(self, source: Vertex) -> Set[Vertex]:
        """
        Using visited to mark the nodes/vertices that have been visited and a queue (fifo) to ensure that the graph is
        traversed one level at a time.
        Since the algorithm traversed the whole graph once, its time complexity is O(V+E) where V is the number of
        vertices & E is the number of edges
        """

        # initialize set for storing already visited vertices/nodes
        visited = set()

        # create a FIFO queue to store all vertices for BFS
        queue = Queue()

        # the graph has no nodes
        if self.node_count == 0:
            return visited

        # since we are starting at the source, we add it to visited
        visited.add(source)
        queue.enqueue(source)

        while not queue.is_empty():
            current_node = queue.dequeue()

            for adjacent_node in self.adjacency_list[current_node]:
                if adjacent_node not in visited:
                    queue.enqueue(adjacent_node)
                    visited.add(adjacent_node)

        return visited

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
