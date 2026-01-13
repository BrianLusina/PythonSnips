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

---

## Connect All Siblings of a Binary Tree

Given the root of a perfect binary tree, where each node is equipped with an additional pointer, next, connect all nodes
from left to right. Do so in such a way that the next pointer of each node points to its immediate right sibling except
for the rightmost node, which points to the first node of the next level.

The next pointer of the last node of the binary tree (i.e., the rightmost node of the last level) should be set to NULL.

> A binary tree in which all the levels are completely filled with nodes, and all leaf nodes (nodes with no children)
> are at the same level.

### Constraints

- The number of nodes in the tree is in the range [0,500].
- -1000 <= `node.data` <= 1000

### Examples

![Example 1](./images/examples/connect_all_siblings_of_binary_tree_example_1.png)
![Example 2](./images/examples/connect_all_siblings_of_binary_tree_example_2.png)

### Solution

The algorithm connects all nodes by utilizing the structure of the perfect binary tree, where each non-leaf node has
exactly two children. Using this property, the algorithm connects nodes without needing extra space. It uses two pointers:
one to traverse the current level and another to connect nodes at the next level. Starting from the root, the algorithm
links each node’s left child to its right child and then connects the right child to the next node’s left child on the
same level, continuing this process across all nodes at that level. If no adjacent node is on the same level, the right
child’s next pointer is connected to the first node on the next lower level. This process continues until all nodes are
connected in a manner that reflects level-order traversal.

The steps of the algorithm are given below:

1. If the root is None, the tree is empty. In this case, return immediately.
2. Initialize two pointers current and last to the root node. The current pointer traverses the nodes level by level,
   while the last keeps track of the last node connected via the next pointer.
3. The loop continues as long as current.left exists. In a perfect binary tree, all non-leaf nodes have a left child,
   so this condition ensures that the loop continues until all levels are processed.
   - First connection: last.next = current.left connects the last node (initially the root) to the current.left child.
     After this, last is updated to current.left.
   - Second connection: last.next = current.right connects current.left (now pointed to by last) to current.right. last
     is then updated to current.right.
   - Move to the next node: current = current.next moves the current pointer to the next node.
4. Finally, return the modified root of the tree, where all nodes are connected to their next sibling in the level-order
   traversal.

Let’s look at the following illustration(s) to get a better understanding of the solution:

![Solution 1](./images/solutions/connect_all_siblings_of_binary_tree_solution_1.png)
![Solution 2](./images/solutions/connect_all_siblings_of_binary_tree_solution_2.png)
![Solution 3](./images/solutions/connect_all_siblings_of_binary_tree_solution_3.png)
![Solution 4](./images/solutions/connect_all_siblings_of_binary_tree_solution_4.png)
![Solution 5](./images/solutions/connect_all_siblings_of_binary_tree_solution_5.png)
![Solution 6](./images/solutions/connect_all_siblings_of_binary_tree_solution_6.png)
![Solution 7](./images/solutions/connect_all_siblings_of_binary_tree_solution_7.png)
![Solution 8](./images/solutions/connect_all_siblings_of_binary_tree_solution_8.png)
![Solution 9](./images/solutions/connect_all_siblings_of_binary_tree_solution_9.png)
![Solution 10](./images/solutions/connect_all_siblings_of_binary_tree_solution_10.png)
![Solution 11](./images/solutions/connect_all_siblings_of_binary_tree_solution_11.png)
![Solution 12](./images/solutions/connect_all_siblings_of_binary_tree_solution_12.png)
![Solution 13](./images/solutions/connect_all_siblings_of_binary_tree_solution_13.png)
![Solution 14](./images/solutions/connect_all_siblings_of_binary_tree_solution_14.png)
![Solution 15](./images/solutions/connect_all_siblings_of_binary_tree_solution_15.png)
![Solution 16](./images/solutions/connect_all_siblings_of_binary_tree_solution_16.png)
![Solution 17](./images/solutions/connect_all_siblings_of_binary_tree_solution_17.png)

#### Time Complexity

The time complexity of the solution is O(N), where N is the number of nodes in the binary tree. The algorithm traverses
each node exactly once, connecting the left and right children as it moves through the tree.

#### Space Complexity

The space complexity of the solution is O(1) because the algorithm uses only a constant amount of extra space,
specifically the pointers current and last, regardless of the size of the tree.
