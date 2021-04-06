# Word Search

Create a program to solve a word search puzzle.

In word search puzzles you get a square of letters and have to find specific words in them.

For example:

```
jefblpepre
camdcimgtc
oivokprjsm
pbwasqroua
rixilelhrs
wolcqlirpc
screeaumgr
alxhpburyi
jalaycalmp
clojurermt
```

There are several programming languages hidden in the above square.

Words can be hidden in all kinds of directions: left-to-right, right-to-left, vertical and diagonal.

Create a program that given a puzzle and a list of words returns the location of the first and last letter of each word.

You will be provided with a Point(x, y) class which will be used to display the points of the first and last words of
the found words.

You will be required to create a method `search` of class WordSearch that takes in a parameter `word` and searches
through the provided grid for this word. It must return the Points of thw first and last letter of the word if found
else return None.

An e.g.

``` python
puzzle = ('jefblpepre\n'
          'camdcimgtc\n'
          'oivokprjsm\n'
          'pbwasqroua\n'
          'rixilelhrs\n'
          'wolcqlirpc\n'
          'screeaumgr\n'
          'alxhpburyi\n'
          'jalaycalmp\n'
          'clojurermt')

>>> example = WordSearch(puzzle)
>>> example.search('clojure')
(Point(0, 9), Point(6, 9))
```

From the above, from the word `clojure`, **c** can be found at point 0,9 and the last letter **e** can be found at poin
6, 9

> Note: indexes start counting from 0.
