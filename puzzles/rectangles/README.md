# Rectangles

Count the rectangles in an ASCII diagram.

Create a program to count the rectangles in an ASCII diagram like the one below.

```
   +--+
  ++  |
+-++--+
|  |  |
+--+--+
```

The above diagram contains 6 rectangles:

```


+-----+
|     |
+-----+
```

```
   +--+
   |  |
   |  |
   |  |
   +--+
```

```
   +--+
   |  |
   +--+


```

```


   +--+
   |  |
   +--+
```

```


+--+
|  |
+--+
```

```

  ++
  ++


```

You may assume that the input is always a proper rectangle (i.e. the length of every line equals the length of the first
line).

You are required to create a function `count`, that accepts a parameter `lines` which will be a list and returns the
number of rectangles.

``` python
>>> lines = ["+-+",
         "| |",
         "+-+",
         ]
>>> count(lines)
>>> 1
```

``` python
>>> lines = ["+------+----+",
         "|      |    |",
         "+------+    |",
         "|   |       |",
         "+---+-------+"
         ]
>>> count(lines)
>>> 2
```

