# Write a function for doing an in-place ↴ shuffle of a list.

The shuffle must be "uniform," meaning each item in the original list must have the same probability of ending up in
each spot in the final list.

Assume that you have a function get_random(floor, ceiling) for getting a random integer that is >= floor and <= ceiling.

Breakdown It helps to start by ignoring the " in-place ↴ " requirement, then adapt the approach to work in-place.

Also, the name "shuffle" can be slightly misleading—the point is to arrive at a random ordering of the items from the
original list. Don't fixate too much on preconceived notions of how you would "shuffle" e.g. a deck of cards.

How might we do this by hand?

We can simply choose a random item to be the first item in the resulting list, then choose another random item (from the
items remaining) to be the second item in the resulting list, etc.

Assuming these choices were in fact random, this would give us a uniform shuffle. To prove it rigorously, we can show
any given item aa has the same probability (\frac{1}{n} ​n ​ ​1 ​​ ) of ending up in any given spot.

First, some stats review: to get the probability of an outcome, you need to multiply the probabilities of all the steps
required for that outcome. Like so:​

So, how do we implement this in code?

If we didn't have the "in place" requirement, we could allocate a new list, then one-by one take a random item from the
input list, remove it, put it in the first position in the new list, and keep going until the input list is empty (well,
probably a copy of the input list—best not to destroy the input)

How can we adapt this to be in-place?

What if we make our new "random" list simply be the front of our input list?

The solution is outlined in the `__init__.py` file

Complexity O(n)O(n) time and O(1)O(1) space.

What We Learned Don't worry, most interviewers won't expect a candidate to know the Fisher-Yates shuffle algorithm.
Instead, they'll be looking for the problem-solving skills to derive the algorithm, perhaps with a couple hints along
the way.

They may also be looking for an understanding of why the naive solution is non-uniform (some outcomes are more likely
than others). If you had trouble with that part, try walking through it again.