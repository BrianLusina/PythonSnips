Given an array of n distinct elements, find the minimum number of swaps required to sort the array.

Examples:

Input : {4, 3, 2, 1} Output : 2 Explanation : Swap index 0 with 3 and 1 with 2 to form the sorted array {1, 2, 3, 4}.

Input : {1, 5, 4, 3, 2} Output : 2

## Reference

Using Graph Theory

Create a graph with n vertices. Create an edge from node n_i to n_j if the element in position i should be in position j
in the correct ordering. You will now have a graph consisting of several non-intersecting cycles. I argue that the
minimum number of swaps needed to order the graph correctly is

M = sum (c in cycles) size(c) - 1 Take a second to convince yourself of that...if two items are in a cycle, one swap can
just take care of them. If three items are in a cycle, you can swap a pair to put one in the right spot, and a two-cycle
remains, etc. If n items are in a cycle, you need n-1 swaps. (This is always true even if you don't swap with immediate
neighbors.)

Given that, you may now be able to see why your algorithm is optimal. If you do a swap and at least one item is in the
right position, then it will always reduce the value of M by 1. For any cycle of length n, consider swapping an element
into the correct spot, occupied by its neighbor. You now have a correctly ordered element, and a cycle of length n-1.

Since M is the minimum number of swaps, and your algorithm always reduces M by 1 for each swap, it must be optimal.

[Link](https://stackoverflow.com/questions/15152322/compute-the-minimal-number-of-swaps-to-order-a-sequence/15152602#15152602)