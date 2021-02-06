Write a function to see if a binary tree is "superbalanced" (a new tree property we just made up).
A tree is "superbalanced" if the difference between the depths of any two leaf nodes

> A leaf node is a tree node with no children.
> It's the "end" of a path to the bottom, from the root.

is no greater than one.

[Reference](https://www.interviewcake.com/question/python/balanced-binary-tree)

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

## Complexity

O(n) time and O(n)O(n) space.

For time, the worst case is the tree is balanced and we have to iterate over all nn nodes to make sure.

For the space cost, we have two data structures to watch: depths and nodes.

depths will never hold more than three elements, so we can write that off as O(1)O(1).

Because we’re doing a depth first search, nodes will hold at most dd nodes where dd is the depth of the tree (the number of levels in the tree from the root node down to the lowest node). So we could say our space cost is O(d)O(d).

But we can also relate dd to nn. In a balanced tree, dd is O(\log_{2}(n))O(log
​2
​​ (n)). And the more unbalanced the tree gets, the closer dd gets to nn.

In the worst case, the tree is a straight line of right children from the root where every node in that line also has a left child. The traversal will walk down the line of right children, adding a new left child to nodes at each step. When the traversal hits the rightmost node, nodes will hold half of the nn total nodes in the tree. Half n is O(n)O(n), so our worst case space cost is O(n)O(n).

## What we learn

This is an intro to some tree basics. If this is new to you, don't worry—it can take a few questions for this stuff to come together. We have a few more coming up.

Particular things to note:

Focus on depth-first ↴ vs breadth-first ↴ traversal. You should be very comfortable with the differences between the two and the strengths and weaknesses of each.

You should also be very comfortable coding each of them up.

One tip: Remember that breadth-first uses a queue ↴ and depth-first uses a stack ↴ (could be the call stack or an actual stack object). That's not just a clue about implementation, it also helps with figuring out the differences in behavior. Those differences come from whether we visit nodes in the order we see them (first in, first out) or we visit the last-seen node first (last in, first out).