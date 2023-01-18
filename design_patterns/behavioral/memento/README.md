Memento is a behavioral design pattern that allows making snapshots of an object’s state and restoring it in future.

The Memento doesn’t compromise the internal structure of the object it works with, as well as data kept inside the
snapshots.

Usage examples: The Memento’s principle can be achieved using serialization, which is quite common in Python. While it’s
not the only and the most efficient way to make snapshots of an object’s state, it still allows storing state backups
while protecting the originator’s structure from other objects.

Conceptual Example
This example illustrates the structure of the Memento design pattern. It focuses on answering these questions:

- What classes does it consist of?
- What roles do these classes play?
- In what way the elements of the pattern are related?
