# Find Closest Value in BST

Write a function that takes in a Binary Search Tree (BST) and a target integer
value and returns the closest value to that target value contained in the BST.

You can assume that there will only be one closest value.

Each <span>BST</span> node has an integer <span>value</span>, a
<span>left</span> child node, and a <span>right</span> child node. A node is
said to be a valid <span>BST</span> node if and only if it satisfies the BST
property: its <span>value</span> is strictly greater than the values of every
node to its left; its <span>value</span> is less than or equal to the values
of every node to its right; and its children nodes are either valid
<span>BST</span> nodes themselves or <span>None</span> / <span>null</span>.

Sample Input:

```text
tree =   10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14
target = 12
```

Sample output: 13

## Hints

- Try traversing the BST node by node, all the while keeping track of the node with the value closest to the target value. 
  Calculating the absolute value of the difference between a node's value and the target value should allow you to 
  check if that node is closer than the current closest one.
- Make use of the BST property to determine what side of any given node has values close to the target value and is 
  therefore worth exploring.
- What are the advantages and disadvantages of solving this problem iteratively as opposed to recursively?

## Optimal Space & Time Complexity

Average: O(log(n)) time | O(1) space where n is the number of nodes in the tree
BST Worst: O(n) time | O(1) space where n is the number of nodes in the tree
