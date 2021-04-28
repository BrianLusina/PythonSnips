# Problem

Implement a function that returns the number of nodes at a given level starting from a root node of a directed graph.

## Input

An undirected graph represented as an adjacency list, and the level whose number of nodes we need to find

## Output
The number of nodes returned as a simple integer

## Explanation
The solution above modifies the visited list to store the level of each node. Later, count the nodes with the same level.

In this code, while visiting each node, the level of that node is set with an increment in the level of its parent node, i.e.,

       visited[child] = visited[parent] + 1 
This is how the level of each node is determined.

## Time complexity
Its time complexity is the same as the breadth-first traversal algorithm. We have added no new loops, just a simple list to do our job.

The time complexity of BFS can be computed as the total number of iterations performed by the loop.

Let EE be the set of all edges in the graph. For each edge {u, v}u,v in EE the algorithm makes two loops iteration steps: one time when the algorithm visits the neighbors of uu and one time when it visits the neighbors of vv.

Hence, the time complexity is OO(VV ++ EE).

