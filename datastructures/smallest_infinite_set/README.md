# Smallest Number in Infinite Set

You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int pop_smallest() Removes and returns the smallest integer contained in the infinite set.
void add_back(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

```plain
Example 1:

Input
["SmallestInfiniteSet", "add_back", "pop_smallest", "pop_smallest", "pop_smallest", "add_back", "pop_smallest", "pop_smallest", "pop_smallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.add_back(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.pop_smallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.pop_smallest(); // return 2, and remove it from the set.
smallestInfiniteSet.pop_smallest(); // return 3, and remove it from the set.
smallestInfiniteSet.add_back(1);    // 1 is added back to the set.
smallestInfiniteSet.pop_smallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.pop_smallest(); // return 4, and remove it from the set.
smallestInfiniteSet.pop_smallest(); // return 5, and remove it from the set.
```

## Constraints:

- 1 <= num <= 1000
- At most 1000 calls will be made in total to pop_smallest and add_back.

## Related Topics

- Hash Table
- Design
- Heap (Priority Queue)
