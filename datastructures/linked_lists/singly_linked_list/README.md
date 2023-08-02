# Singly Linked list

## You have a singly-linked list and want to check if it contains a cycle.

A singly-linked list is built with nodes, where each node has:

node.next—the next node in the list. node.value—the data held in the node. For example, if our linked list stores people
in line at the movies, node.value might be the person's name. For example:

``` python
  class LinkedListNode:

    def __init__(cls, value):
        cls.value = value
        cls.next  = None
```

A cycle occurs when a node’s next points back to a previous node in the list. The linked list is no longer linear with a
beginning and end—instead, it cycles through a loop of nodes.

Write a function contains_cycle() that takes the first node in a singly-linked list and returns a boolean indicating
whether the list contains a cycle.

Because a cycle could result from the last node linking to the first node, we might need to look at every node before we
even see the start of our cycle again. So it seems like we can’t do better than O(n) runtime.

How can we track the nodes we’ve already seen?

Using a set, we could store all the nodes we’ve seen so far. The algorithm is simple:

If the current node is already in our set, we have a cycle. Return True. If the current node is None we've hit the end
of the list. Return False. Else throw the current node in our set and keep going. What are the time and space costs of
this approach? Can we do better?

Our runtime is O(n), the best we can do. But our space cost is also O(n). Can we get our space cost down to O(1) by
storing a constant number of nodes?

Think about a looping list and a linear list. What happens when you traverse one versus the other?

A linear list has an end—a node that doesn’t have a next node. But a looped list will run forever. We know we don’t have
a loop if we ever reach an end node, but how can we tell if we’ve run into a loop?

We can’t just run our function for a really long time, because we’d never really know with certainty if we were in a
loop or just a really long list.

Imagine that you're running on a long, mountainous running trail that happens to be a loop. What are some ways you can
tell you're running in a loop?

One way is to look for landmarks. You could remember one specific point, and if you pass that point again, you know
you’re running in a loop. Can we use that principle here?

Well, our cycle can occur after a non-cyclical "head" section in the beginning of our linked list. So we'd need to make
sure we chose a "landmark" node that is in the cyclical "tail" and not in the non-cyclical "head." That seems impossible
unless we already know whether or not there's a cycle...

Think back to the running trail. Besides landmarks, what are some other ways you could tell you’re running in a loop?
What if you had another runner? (Remember, it’s a singly-linked list, so no running backwards!)

A tempting approach could be to have the other runner stop and act as a "landmark," and see if you pass her again. But
we still have the problem of making sure our "landmark" is in the loop and not in the non-looping beginning of the
trail.

What if our "landmark" runner moves continuously but slowly?

If we sprint quickly down the trail and the landmark runner jogs slowly, we will eventually "lap" (catch up to) the
landmark runner!

But what if there isn't a loop?

Then we (the faster runner) will simply hit the end of the trail (or linked list).

So let's make two variables, slow_runner and fast_runner. We’ll start both on the first node, and every time slow_runner
advances one node, we’ll have fast_runner advance two nodes.

If fast_runner catches up with slow_runner, we know we have a loop. If not, eventually fast_runner will hit the end of
the linked list and we'll know we don't have a loop.

This is a complete solution! Can you code it up?

Make sure the function eventually terminates in all cases!

## Solution

We keep two pointers to nodes (we'll call these “runners”), both starting at the first node. Every time slow_runner
moves one node ahead, fast_runner moves two nodes ahead.

If the linked list has a cycle, fast_runner will "lap" (catch up with) slow_runner, and they will momentarily equal each
other.

If the list does not have a cycle, fast_runner will reach the end.

### Complexity

O(n) time and O(1)O(1) space.

The runtime analysis is a little tricky. The worst case is when we do have a cycle, so we don't return until fast_runner
equals slow_runner. But how long will that take?

First, we notice that when both runners are circling around the cycle fast_runner can never skip over slow_runner. Why
is this true?

Suppose fast_runner had just skipped over slow_runner. fast_runner would only be 1 node ahead of slow_runner, since
their speeds differ by only 1. So we would have something like this:

[ ] -> [s] -> [f]
What would the step right before this "skipping step" look like? fast_runner would be 2 nodes back, and slow_runner
would be 1 node back. But wait, that means they would be at the same node! So fast_runner didn't skip over
slow_runner! (This is a proof by contradiction.)

Since fast_runner can't skip over slow_runner, at most slow_runner will run around the cycle once and fast_runner will
run around twice. This gives us a runtime of O(n)O(n).

For space, we store two variables no matter how long the linked list is, which gives us a space cost of O(1)O(1).

### Bonus

How would you detect the first node in the cycle? Define the first node of the cycle as the one closest to the head of
the list. Would the program always work if the fast runner moves three steps every time the slow runner moves one step?
What if instead of a simple linked list, you had a structure where each node could have several "next" nodes? This data
structure is called a "directed graph." How would you test if your directed graph had a cycle? What We Learned Some
people have trouble coming up with the "two runners" approach. That's expected—it's somewhat of a blind insight. Even
great candidates might need a few hints to get all the way there. And that's fine.

Remember that the coding interview is a dialogue, and sometimes your interviewer expects she'll have to offer some hints
along the way.

One of the most impressive things you can do as a candidate is listen to a hint, fully understand it, and take it to its
next logical step.

---

## Delete the middle Node of a Linked List

You are given the head of a linked list. Delete the middle node, and return the middle node of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

```plain
Example 1:

Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
```

```plain
Example 2:

Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
```

```plain
Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.
```

### Solution(s)

#### Approach 1: 2 Passes

##### Intuition

Let's start with a simple approach.

We make the first iteration, starting from head, going through the entire linked list and getting the total number of
nodes (let's say `node_count`). According to the definition provided, the index of the middle node is:
`middleIndex=floor(node_count / 2)−1`.

Now we make a second iteration to the `predecessor` node of the middle node, which means that we stop at index
`middleIndex - 1`.

Once we reach the predecessor node of the middle node, we can remove the middle node from the linked list.

##### Algorithm

1. If there is only one node, return None.
2. Otherwise, initialize two pointers p1 = head and p2 = head.
3. Iterate the linked list with p1 and count the total number of nodes it has (count).
4. Let p2 move forward by floor(node_count / 2) - 1 nodes, now it is the predecessor of the middle node, delete the
   middle node. Return the middle node.

```python
from typing import Optional
from datastructures.linked_lists.singly_linked_list.node import SingleNode


def delete_middle_node(head: SingleNode) -> Optional[SingleNode]:
    if not head or not head.next:
        return None

    # Node count here is obtained which results in O(n)
    node_count = 0
    p1 = p2 = head
    while p1:
        node_count += 1
        p1 = p1.next

    middle_index = node_count // 2

    # traversing half the linked list to get to the predecessor of the middle node(i.e. the node before the middle node)
    for _ in range(middle_index - 1):
        p2 = p2.next

    # we have the middle node, now we assign it and return it later
    middle_node = p2.next

    # deleting is handled by moving the next pointer of the predecessor to the next pointer of the middle node
    p2.next = p2.next.next

    return middle_node
```

> Note that this has been implemented in the [SinglyLinkedList](__init__.py) class but with slight modifications

##### Complexity Analysis

Let `n` be the length of the input linked list.

1. `Time complexity: O(n)`

    - We iterate over the linked list twice, the first time traversing the entire linked list and the second traversing
      half of it. Hence there are a total of `O(n)` steps.
    - In each step, we move a pointer forward by one node, which takes constant time.
    - Remove the middle node takes a constant amount of time.
    - In summary, the overall time complexity is `O(n)`.

2. `Space complexity: O(1)`

    - We only need two pointers, thus the space complexity is `O(1)`.

#### Approach 2: 2 Pointers

##### Intuition

The key of this approach is that we have two pointers `fast` and `slow` traversing the linked list at the same time, and
`fast` traverses twice as fast as `slow`. Therefore, when `fast` reaches the end of the linked list, `slow` is right in
the middle! We only need one iteration to reach the middle node!

All that needs to be determined are a few lookup details. If there is only one node in the linked list, this node is
also the one to be deleted and there are no nodes left after the deletion. Therefore, instead of initializing two
pointers for the following procedure, we can just return null.

> Why we initialize fast = head.next.next at the beginning?

The reason for this is that we want to delete the middle node instead of finding it. Therefore, we are actually looking
for the `predecessor` of the middle node, not the middle node itself, or rather, this is like moving slow backward one
node after the iteration stops.

Certainly, we can't move a pointer backward on a singly linked list, thus we can show this one less step on `slow` by
letting `fast` moves forward one more step (by two nodes, of course). Hence, `slow` will also point to the predecessor
node of the middle node (rather than the middle node) at the end of the iteration.

##### Algorithm

1. If there is only one node, return null.
2. Otherwise, initialize two pointers `slow` and `fast`, with slow pointing to head and fast pointing to the second
   successor node of head.
3. While neither `fast` and `fast.next` is `null`:
    - we move `fast` forward by 2 nodes.
    - we move `slow` forward by 1 node.
4. Now `slow` is the predecessor of the middle node, delete the middle node.
5. Return middle node.

```python
from typing import Optional
from datastructures.linked_lists.singly_linked_list.node import SingleNode


def delete_middle_node_2_pointers(head: Optional[SingleNode]) -> Optional[SingleNode]:
    if not head or not head.next:
        return None

    slow, fast = head, head.next.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    middle_node = slow.next

    slow.next = slow.next.next

    return middle_node
```

> Note that the implementation outlined here is what is denoted in the instance method `delete_middle_node_2_pointers`
> of the class [SinglyLinkedList](__init__.py) with some slight modifications

##### Complexity Analysis

1. `Time Complexity O(n)`
    - We stop the iteration when the pointer fast reaches the end, fast moves forward 2 nodes per step, so there are at
      most `n/2` steps.
    - In each step, we move both `fast` and `slow`, which takes a constant amount of time.
    - Removing the middle node also takes constant time.
    - In summary, the overall time complexity is `O(n)`.

2. `Space Complexity O(1)`

    - We only need 2 pointers, so the space complexity is `O(1)`

---

### Related Topics

- Linked List
- Two Pointers