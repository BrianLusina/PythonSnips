# heapsort

Contains heapsort implementation

Complexity

For the heapify step, we're examining every item in the tree and moving it downwards until it's larger than its
children. Since our tree height is O(lg(n)), we could do up to O(lg(n)) moves. Across all n nodes, that's an overall
time complexity of O(nlg(n)).

We've shown that the heapify step is O(nlg(n)). With a bit more complex analysis, it turns out to actually be O(n).

After transforming the tree into a heap, we remove all nn elements from it—one item at a time. Removing from a heap
takes O(lg(n)) time, since we have to move a new value to the root of the heap and bubble down. Doing n remove
operations will be O(nlg(n)) time.

Is this analysis too pessimistic? Each time we remove an item from the heap it gets smaller, so won't later removes be
cheaper than earlier ones?

A more thorough analysis shows that doing n removals is still O(nlg(n))

Putting these steps together, we're at O(nlg(n)) time in the worst case (and on average).

But what happens if all the items in the input are the same?

Every time we remove an element from the tree root, the item replacing it won't have to bubble down at all. In that
case, each remove takes O(1)O(1) time, and doing nn remove operations takes O(n).

So the best case time complexity is O(n)O(n). This is the runtime when everything in the input is identical.

Since we cleverly reused available space at the end of the input list to store the item we removed, we only need O(1)O(
1) space overall for heapsort.