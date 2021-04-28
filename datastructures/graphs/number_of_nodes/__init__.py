from datastructures.queues.fifo import FifoQueue


class AdjNode:
    """
    A class to represent the adjacency list of the node
    """

    def __init__(self, data):
        """
        Constructor
        :param data : vertex
        """
        self.data = data
        self.next = None


class Graph:
    """
    Graph Class ADT
    """

    def __init__(self, vertices):
        """
        Constructor
        :param vertices : Total vertices in a graph
        """
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, source, destination):
        """
        add edge
        :param source: Source Vertex
        :param destination: Destination Vertex
        """

        # Adding the node to the source node
        node = AdjNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node

        # Adding the source node to the destination if undirected graph

        # Intentionally commented the lines
        # node = AdjNode(source)
        # node.next = self.graph[destination]
        # self.graph[destination] = node

    def print_graph(self):
        """
        A function to print a graph
        """
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


def number_of_nodes(graph: Graph, level: int):
    """
    Counts the number of nodes at a given level
    :param graph: Graph
    :param level: Level
    :return: Number of nodes at a given level
    """
    source = 0
    visited = [0] * len(graph.graph)

    queue = FifoQueue()

    # mark the source node as visited & enqueue it
    queue.enqueue(source)
    visited[source] = 1

    while not queue.is_empty():
        # dequeue a vertex/node from the queue
        source = queue.dequeue()

        # Get all adjacent vertices of the dequeued vertex. If adjacent vertex has not been visited, then mark it
        # visited & enqueue it

        while graph.graph[source] is not None:
            data = graph.graph[source].data

            if visited[data] == 0:
                queue.enqueue(data)
                visited[data] = visited[source] + 1

            graph.graph[source] = graph.graph[source].next

    # counting the number of nodes at a given level
    result = 0

    for x in range(len(graph.graph)):
        if visited[x] == level:
            result += 1

    return result
