# Binary Trees

## Lowest Common Ancestor of a Binary Tree

You are given two nodes, p and q. The task is to return their lowest common ancestor (LCA). Both nodes have a reference 
to their parent node. The tree’s root is not provided; you must use the parent pointers to find the nodes’ common 
ancestor.

> Note: The lowest common ancestor of two nodes, p and q, is the lowest node in the binary tree, with both p and q as 
> descendants. In a tree, a descendant of a node is any node reachable by following edges downward from that node, 
> including the node itself.

Constraints

- -10^4 ≤ `node.data` ≤ 10^4
- The number of nodes in the tree is in the range [2, 500]
- All `node.data` are unique
- `p` != `q`
- Both `p` and `q` are present in the tree

### Examples

![Example 1](./images/examples/lowest_common_ancestor_example_1.png)
![Example 2](./images/examples/lowest_common_ancestor_example_2.png)
![Example 3](./images/examples/lowest_common_ancestor_example_3.png)
![Example 4](./images/examples/lowest_common_ancestor_example_4.png)

### Solution

This solution finds the lowest common ancestor (LCA) of two nodes in a binary tree using a smart two-pointer approach. 
We start by placing one pointer at node p and the other at node q. Both pointers move up the tree at each step by 
following their parent pointers. If a pointer reaches the root (i.e., its parent is None), it jumps to the other 
starting node. This process continues until the two pointers meet. The key idea is that by switching starting points 
after reaching the top, both pointers end up traveling the same total distance, even if p and q are at different depths.
When they meet, that meeting point is their lowest common ancestor.

The steps of the algorithm are as follows:

1. Initialize two pointers: `ptr1` starting at `p` and `ptr2` starting at `q`. 
2. While `ptr1` and `ptr2` are not pointing to the same node:
   - If `ptr1` has a parent, move `ptr1` to `ptr1.parent;` otherwise, set `ptr1 = q`.
   - If `ptr2` has a parent, move `ptr2` to `ptr2.parent`; otherwise, set `ptr2 = p`.

3. When `ptr1 == ptr2`, return `ptr1`. This node is the lowest common ancestor (LCA) of p and q.

Let’s look at the following illustration to get a better understanding of the solution:

![Solution 1](./images/solutions/lowest_common_ancestor_solution_1.png)
![Solution 2](./images/solutions/lowest_common_ancestor_solution_2.png)
![Solution 3](./images/solutions/lowest_common_ancestor_solution_3.png)
![Solution 4](./images/solutions/lowest_common_ancestor_solution_4.png)
![Solution 5](./images/solutions/lowest_common_ancestor_solution_5.png)
![Solution 6](./images/solutions/lowest_common_ancestor_solution_6.png)
![Solution 7](./images/solutions/lowest_common_ancestor_solution_7.png)

### Complexity

#### Time Complexity

The time complexity is `O(h)` where `h` is the height of the tree, as in the worst case, each pointer might traverse the 
entire height of the tree, including `h` steps.

#### Space complexity

The space complexity of this solution is `O(1)` as there is no additional space being used. Only two pointers are being 
maintained requiring constant space.

