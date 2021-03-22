from datastructures.graphs.directed import DirectedGraph
from datastructures.graphs import Node

connections = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')]

directed_graph = DirectedGraph(connections)

print(directed_graph)

node1 = Node("A")
node2 = Node("B")

print(f"All paths: {directed_graph.find_all_paths(node1, node2)}")
