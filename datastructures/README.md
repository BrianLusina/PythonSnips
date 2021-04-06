# Data Structures and Algorithms

Snippets involving various Data Structures and Algorithms in Python :snake:.

### QueueTwoStacks

Implement a [queue](./queues/README.md) with 2 [stacks](./stacks/README.md). Your queue should have an enqueue and
dequeue function and it should be `FIFO`.

Each enqueue is O(1) time and so is each dequeue when out_stack has items. Dequeue on an empty out_stack is order of the
number of items in in_stack at that moment, which can vary significantly.

Notice that the more expensive a dequeu on an empty out_stack is (i.e. the more items we have to move from in_stack to
out_stack), the more O(1)-time dequeues off of a non-empty out_stack it wins us in the future. Once items are moved from
in_stack to out_stack they just sit there, ready to be dequeued in O(1) time. An item never moves *'backwards'* in our
data structure.

We might guess that this averages out so that in a set of m enqueues and dequeues the total cost of all dequeues is
actually just O(m). To check this rigorously, we can use the `accounting method`

> The accounting method can be used for computing time complexity for things link 'the cost of m operations on this data structure'. In the accounting method, you simply look at the time cost incurred by each item passing through the system instead of the time cost of each operation.


Accounting method will count the time cost per item instead of per enqueue or dequeue

So, the worst case for a single item. which is the case where it is enqueue and then later dequeued. In this case, the
item enters in_stack(costing 1 push), then later moves to out_stack(costing 1pop and 1 push) then later comes off
out_stack to get returned(costing 1 pop)

Each of these 4 pushes and pops is O(1) time. So out total cost per item is O(1). Our m enqueue and dequeue operations
put m or fewer items into the system, giving a total runtime of O(m)!

The trick is to think of the cost per item passing through our queue, rather thatn the cost per enqueue and dequeue

This trick comes in handy when you're looking at the time cost of not just one function call, but 'm' function calls.
