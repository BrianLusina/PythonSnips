Write a function to see if a binary tree is "superbalanced" (a new tree property we just made up).
A tree is "superbalanced" if the difference between the depths of any two leaf nodes

> A leaf node is a tree node with no children.
> It's the "end" of a path to the bottom, from the root.

is no greater than one.

[Reference](https://www.interviewcake.com/question/python/balanced-binary-tree?utm_source=weekly_email&utm_campaign=weekly_email&utm_medium=email)

We do a depth-first walk through our tree, keeping track of the depth as we go. When we find a leaf, we throw its depth into a list of depths if we haven't seen that depth already.

```
Depth-first traversal is a method for walking through a tree or graph where you go as deep as possible down a path before "fanning out." Your set of visited nodes will shoot out from the starting point along one path, with more single paths progressively shooting off of that one as each path hits a dead end.
Depth-first search or DFS uses depth-first traversal to search for something in a tree or graph.
Depth-first traversal is often compared with breadth-first traversal.

Advantages:
+ Depth-first traversal on a binary tree generally requires less memory than breadth-first.
+ Depth-first traversal can be easily implemented with recursion.

Disadvantages
+ A DFS doesn't necessarily find the shortest path to a node, while breadth-first search does.
```

Each time we hit a leaf with a new depth, there are two ways that our tree might now be unbalanced:

There are more than 2 different leaf depths
There are exactly 2 leaf depths and they are more than 1 apart.
Why are we doing a depth-first walk and not a breadth-first ↴ one? You could make a case for either. We chose depth-first because it reaches leaves faster, which allows us to short-circuit earlier in some cases.

```
Breadth-first traversal is a method for walking through a tree or graph where you "fan out" as much as possible before going deeper. Your set of visited nodes will seem to "ripple outwards" from the starting point.

Breadth-first search or BFS uses breadth-first traversal to search for something in a tree or graph.

Breadth-first traversal is often compared with depth-first traversal.

Advantages:

A BFS will not necessarily find a target as quickly as possible, but it will find the shortest path between the starting point and the target. A depth-first search will not necessarily find the shortest path.
Disadvantages

A BFS on a binary tree generally requires more memory than a DFS.
```

