Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1

Input: n = 3 
Output: 5
For n = 3, preorder traversal of Unique BSTs are:
1. 1 2 3
2. 1 3 2
3. 2 1 3
4. 3 1 2
5. 3 2 1

Input: 4 
Output: 14

For all possible values of i, consider i as root, then [1….i-1] numbers will fall in the left subtree and [i+1….n] numbers will fall in the right subtree. So, add (i-1)*(n-i) to the answer. The summation of the products will be the answer to the number of unique BST.