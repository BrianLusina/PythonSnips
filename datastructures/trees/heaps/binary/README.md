# Binary Heap

This demonstrates the implementation of a binary heap in Python. There are 2 kinds of binary heaps:

1. Max Heap
2. Min Heap

## Conditions

The heap is a binary tree that maintains the following conditions:

1. The value of each node must be greater or less than(depending on the type of heap implementation) each of its
   descendant nodes. This is known as the _heap
   condition_
2. The tree must be _complete_. This is important because we want to ensure our heap remains well-balanced when
   performing insertion and deletions. This is also important as it allows the datastructure to achieve _O(log N)_
   operations making it fast.

## Properties

1. Heaps are _weakly ordered_, meaning that it would not be clear where to search for a particular element. Given an
   element to search for, it would not be straight forward whether to search the left or the right
2. The root node will always either have the _greatest_ or the _smallest_ value, depending on whether it is a **max-heap
   ** or a **min-heap** respectively
3. Heaps primary have 2 operations; _insert_  _delete_, since searching through a heap would require inspecting all
   nodes, making it inefficient for search, it is not usually implemented. However, it has a _read_ operation which is
   used to read the root node's value.
4. Heaps have a _last node_, which is the rightmost node in the bottom level.

## Implementation

Heaps are usually _implemented using arrays_ because finding the last node is critical to the heap's operations and we
want to make sure finding the last node is efficient. Using an array allows the datastructure to solve the _problem of
the last node_, which means that the last node will always be the last element in the array.
