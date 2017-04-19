Write a function to check that a binary tree ↴ is a valid binary search tree ↴

```
A binary search tree is a binary tree in which, for each node:

The node's value is greater than all values in the left subtree.
The node's value is less than all values in the right subtree.
BSTs are useful for quick lookups. If the tree is balanced, we can search for a given value in the tree in O(\lg{n})O(lgn) time.

```

We do a depth-first walk through the tree, testing each node for validity as we go. A given node is valid if it's greater than all the ancestral nodes it's in the right sub-tree of and less than all the ancestral nodes it's in the left-subtree of. Instead of keeping track of each ancestor to check these inequalities, we just check the largest number it must be greater than (its lower_bound) and the smallest number it must be less than (its upper_bound).

O(n) time and O(n)O(n) space.

The time cost is easy: for valid binary search trees, we’ll have to check all nn nodes.

Space is a little more complicated. Because we’re doing a depth first search, node_and_bounds_stack will hold at most dd nodes where dd is the depth of the tree (the number of levels in the tree from the root node down to the lowest node). So we could say our space cost is O(d)O(d).

But we can also relate dd to nn. In a balanced tree, dd is \log_{2}{n}log
​2
​​ n. And the more unbalanced the tree gets, the closer dd gets to nn.

In the worst case, the tree is a straight line of right children from the root where every node in that line also has a left child. The traversal will walk down the line of right children, adding a new left child to the stack at each step. When the traversal hits the rightmost node, the stack will hold half of the nn total nodes in the tree. Half n is O(n)O(n), so our worst case space cost is O(n)O(n).

Bonus
What if the input tree has duplicate values?

What We Learned
We could think of this as a greedy ↴ approach. We start off by trying to solve the problem in just one walk through the tree. So we ask ourselves what values we need to track in order to do that. Which leads us to our stack that tracks upper and lower bounds.

We could also think of this as a sort of "divide and conquer" approach. The idea in general behind divide and conquer is to break the problem down into two or more subproblems, solve them, and then use that solution to solve the original problem.

In this case, we're dividing the problem into subproblems by saying, "This tree is a valid binary search tree if the left subtree is valid and the right subtree is valid." This is more apparent in the recursive formulation of the answer above.

Of course, it's just fine that our approach could be thought of as greedy or could be thought of as divide and conquer. It can be both. The point here isn't to create strict categorizations so we can debate whether or not something "counts" as divide and conquer.

Instead, the point is to recognize the underlying patterns behind algorithms, so we can get better at thinking through problems.

Sometimes we'll have to kinda smoosh together two or more different patterns to get our answer.

Reference
[https://www.interviewcake.com/question/python/bst-checker?utm_source=weekly_email&utm_campaign=weekly_email&utm_medium=email](https://www.interviewcake.com/question/python/bst-checker?utm_source=weekly_email&utm_campaign=weekly_email&utm_medium=email)