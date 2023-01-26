# Template Method

Template Method is a behavioral design pattern that allows you to defines a skeleton of an algorithm in a base class and
let subclasses override the steps without changing the overall algorithm’s structure.

Usage examples: The Template Method pattern is quite common in Python frameworks. Developers often use it to provide
framework users with a simple means of extending standard functionality using inheritance.

Identification: Template Method can be recognized if you see a method in base class that calls a bunch of other methods
that are either abstract or empty.