from datastructures.graphs import Node
from datastructures.graphs.directed import DirectedGraph

connections = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C'), ('C', 'A')]

directed_graph = DirectedGraph(connections)

print(directed_graph)

node1 = Node("A")
node2 = Node("B")

print(f"All paths: {directed_graph.find_all_paths(node1, node2)}")

print(f"Contains Cycle: {directed_graph.contains_cycle()}")
