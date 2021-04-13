A linked list is a low-level data structure. It stores an ordered list of items in individual "node" objects that have
pointers to other nodes.

In a singly linked list, the nodes each have one pointer to the next node.

``` python
  class LinkedListNode:

    def __init__(cls, value):
        cls.value = value
        cls.next  = None
```

So we could build a singly linked list like this:

``` python
a = LinkedListNode(5)
b = LinkedListNode(1)
c = LinkedListNode(9)

a.next = b
b.next = c
```

![linked list](https://www.interviewcake.com/images/svgs/linked_list__nodes_and_pointers.svg?bust=135)

A singly-linked list with 3 nodes. The first node has value 5 and an arrow pointing to the second node, which has value
1 and an arrow pointing to the third node, which has value 9 and and arrow pointing to "None."

In a linked list, the first node is called the head and the last node is called the tail.

A linked list with 3 nodes. The first node is labelled "head" and the last node is labelled "tail."

![head tail](https://www.interviewcake.com/images/svgs/linked_list__nodes_and_pointers_labeled_head_and_tail.svg?bust=135)

Often, our only connection to the list itself is a variable pointing to the head. From there we can walk down the list
to all the other nodes.

Like linked lists, arrays also store ordered lists of items, so you usually have a choice of which one to use.

### Advantages of linked lists:

1. Linked lists have constant-time insertions and deletions in any position (you just change some pointers). Arrays
   require O(n)O(n) time to do the same thing, because you'd have to "shift" all the subsequent items over 1 index.

2. Linked lists can continue to expand as long as there is space on the machine. Arrays (in low-level languages) must
   have their size specified ahead of time. Even in languages with "dynamic arrays" that automatically resize themselves
   when they run out of space (like Python, Ruby and JavaScript), the operation to resize a dynamic array has a large
   cost which can make a single insertion unexpectedly expensive.

### Disadvantages of linked lists:

1. To access or edit an item in a linked list, you have to take O(i)O(i) time to walk from the head of the list to the
   iith item (unless of course you already have a pointer directly to that item). Arrays have constant-time lookups and
   edits to the iith item. Another type of linked list is a doubly linked list, which has pointers to the next and the
   previous nodes.

``` python
  class LinkedListNode:

    def __init__(cls, value):
        cls.value    = value
        cls.next     = None
        cls.previous = None
```

So we could build a doubly linked list like this:

``` python
a = LinkedListNode(5)
b = LinkedListNode(1)
c = LinkedListNode(9)

# put b after a
a.next = b
b.previous = a

# put c after b
b.next = c
c.previous = b
```

![doubly linked list](https://www.interviewcake.com/images/svgs/linked_list__doubly_linked_nodes_and_pointers.svg?bust=135)

A doubly-linked list with 3 nodes. The first node has value 5 with a "next" arrow pointing ahead to the second node and
a "previous" arrow pointing back to "None." The second node has value 1 with a "next" arrow pointing ahead to the third
node and a "previous" arrow pointing bacl to the first node. The third node has value 9 with a "next" arrow pointing
ahead to "None" and a "previous" arrow pointing back to the second node.

Doubly linked lists allow us to traverse our list backwards. In a singly linked list, if you just had a pointer to a
node in the middle of a list, there would be no way to know what its previous node was. Not a problem in a doubly linked
list.