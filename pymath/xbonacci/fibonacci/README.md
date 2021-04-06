Create a list to store the fibonacci sequence numbers add the first 2 numbers to the list, add them to get the third
create a counter variable to be used in the while loop, that will evaluate to false to avoid an infinite loop This
counter variable will also be used to iterate through the list adding consecutive numbers break out of loop if next
number is greater than end

## Nth Fibonacci

Write a function fib() that a takes an integer nn and returns the nnth fibonacci ↴ number. Let's say our fibonacci
series is 0-indexed and starts with 0. So:

```plain
fib(0) # => 0
fib(1) # => 1
fib(2) # => 1
fib(3) # => 2
fib(4) # => 3
...
```

Our solution runs in N time.

There's a clever, more mathey solution that runs in O(\lg{n})O(lgn) time, but we'll leave that one as a bonus.

If you wrote a recursive function, think carefully about what it does. It might do repeat work, like computing fib(2)
multiple times!

We can do this in O(1)O(1) space. If you wrote a recursive function, there might be a hidden space cost in the call
stack ↴ !