Write a function that should take its not always "clean" speech and cover as much as possible of it, in order not to
offend some more sensible spirits.

For example, given an input like

```python
What
the
hell
am
I
doing
here? And
where is my
wallet? PETE
SMASH!
```

You are expected to turn it into something like:

```python
W ** t
t * e
h ** l
am
i
d ** * g
h ** e? A * d
w ** * e is my
w ** ** t? P ** e
s ** * h!
```

In case you didn't figure out the rules yet: any words longer than 2 characters need to have its "inside" (meaning every
character which is not the first or the last) changed into *; as we do not want Pete to scream too much, every uppercase
letter which is not at the beginning of the string or coming after a punctuation mark among [".","!","?"] needs to be
put to lowercase; spaces and other punctuation marks can be ignored.

Conversely, you need to be sure that the start of each sentence has a capitalized word at the beginning. Sentences are
divided by the aforementioned punctuation marks.

Finally, the function will take an additional parameter consisting of an array/list of allowed words which are not to be
replaced.

> ALGORITHMS REGULAR EXPRESSIONS DECLARATIVE PROGRAMMING ADVANCED LANGUAGE FEATURES FUNDAMENTALS STRINGS
