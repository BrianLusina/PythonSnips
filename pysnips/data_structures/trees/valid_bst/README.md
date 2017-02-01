Write a function to check that a binary tree ↴ is a valid binary search tree ↴

```
A binary search tree is a binary tree in which, for each node:

The node's value is greater than all values in the left subtree.
The node's value is less than all values in the right subtree.
BSTs are useful for quick lookups. If the tree is balanced, we can search for a given value in the tree in O(\lg{n})O(lgn) time.

```

We do a depth-first walk through the tree, testing each node for validity as we go. A given node is valid if it's greater than all the ancestral nodes it's in the right sub-tree of and less than all the ancestral nodes it's in the left-subtree of. Instead of keeping track of each ancestor to check these inequalities, we just check the largest number it must be greater than (its lower_bound) and the smallest number it must be less than (its upper_bound).


Reference
[https://www.interviewcake.com/question/python/bst-checker?utm_source=weekly_email&utm_campaign=weekly_email&utm_medium=email](https://www.interviewcake.com/question/python/bst-checker?utm_source=weekly_email&utm_campaign=weekly_email&utm_medium=email)