# Design an LRU cache

## Constraints and assumptions

- What are we caching?
    We are cahing the results of web queries
- Can we assume inputs are valid or do we have to validate them?
    Assume they're valid
- Can we assume this fits memory?
    Yes

## Solution

A hash map alone gives us `O(1)` key-value lookup, but doesn't track order. An array tracks order, but inserting/removing
from the middle is `O(n)`. We need a data structure that supports `O(1)` insertion, deletion, AND reordering. This
points us toward a structure where we can move items to the front/back instantly. Think of a playlist where songs move
to the top when played: - When you play a song (access), it jumps to position #1 - When you add a new song and the
playlist is full, the song at the bottom (least recently played) gets removed - You need to find any song by name
instantly (hash map), but also know which song is at the bottom (ordering) This dual requirement - fast lookup by key
AND fast reordering - suggests combining two data structures: one for `O(1)` key access, another for `O(1)` position
changes.

### HashMap + Doubly Linked List hybrid

When you need O(1) access AND O(1) ordering operations (move to front/back, remove),
combine a hash map for lookups with a doubly linked list for order tracking. The hash map stores pointers to list nodes,
enabling instant node location and manipulation.

### Sentinel nodes eliminate edge cases

Use dummy head and tail nodes in your doubly linked list to avoid null checks when adding/removing nodes at boundaries.
This means every real node always has non-null prev/next pointers, simplifying insertion and deletion logic dramatically.

### Access equals update pattern:

In LRU cache, every get() operation must update recency by moving the accessed node to the most-recent position
(typically the head or tail). Forgetting this is the most common bug - reads aren't passive in cache implementations.

### Capacity check timing matters

Always check capacity and evict after inserting the new element, not before. For updates (key exists), no eviction is
needed. For new insertions at capacity, evict the LRU item, then add - this handles the edge case where capacity=1
correctly.

### Bidirectional pointer maintenance

When manipulating doubly linked list nodes, always update four pointers in the correct order: the node's prev/next AND
its neighbors' pointers. A common pattern is to extract a node (reconnect its neighbors), then insert it elsewhere
(update new neighbors and the node itself).

### Cache eviction policy abstraction

This LRU pattern extends to LFU (Least Frequently Used), MRU (Most Recently Used), and TTL caches. The core insight -
combining hash map for O(1) lookup with an auxiliary structure (list, heap, or multiple lists) for O(1) policy
enforcement - applies broadly to cache replacement algorithms.

## Complexity Analysis

### Time Complexity

O(1) Both get and put operations involve hash map lookup (O(1)), and linked list node 
insertion/deletion/movement (O(1) with doubly linked list). No iteration through the cache is needed.

### Space Complexity

O(capacity) We store at most 'capacity' key-value pairs in the hash map, and the same number of nodes in the doubly
linked list. Space grows linearly with capacity.
