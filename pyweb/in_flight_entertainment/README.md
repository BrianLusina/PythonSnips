You've built an in-flight entertainment system with on-demand movie streaming. Users on longer flights like to start a
second movie right when their first one ends, but they complain that the plane usually lands before they can see the
ending. So you're building a feature for choosing two movies whose total runtimes will equal the exact flight length.

Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes) and
returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

When building your function:

+ Assume your users will watch exactly two movies
+ Don't make your users watch the same movie twice
+ Optimize for runtime over memory

Breakdown How would we solve this by hand? We know our two movie lengths need to sum to flight_length. So for a given
first_movie_length, we need a second_movie_length that equals flight_length - first_movie_length.

To do this by hand we might go through movie_lengths from beginning to end, treating each item as first_movie_length,
and for each of those check if there's a second_movie_length equal to flight_length - first_movie_length.

How would we implement this in code? We could nest two loops (the outer choosing first_movie_length, the inner choosing
second_movie_length). That’d give us a runtime of O(n^2)O(n ​2 ​​ ). We can do better.

To bring our runtime down we'll probably need to replace that inner loop (the one that looks for a matching
second_movie_length) with something faster.

We could sort the movie_lengths first—then we could use binary search ↴ A binary search algorithm finds an item in a
sorted list in O(\lg{n})O(lgn) time.

A brute force search would walk through the whole list, taking O(n)O(n) time in the worst case.

Let's say we have a sorted list of numbers. To find a number with a binary search, we:

Start with the middle number: is it bigger or smaller than our target number? Since the list is sorted, this tells us if
the target would be in the left half or the right half of our list. We've effectively divided the problem in half. We
can "rule out" the whole half of the list that we know doesn't contain the target number. Repeat the same approach (of
starting in the middle) on the new half-size problem. Then do it again and again, until we either find the number or "
rule out" the whole set. We can do this recursively, or iteratively. Here's an iterative version:

``` python
  def binary_search(target, nums):
    # see if target appears in nums

    # we think of floor_index and ceiling_index as "walls" around
    # the possible positions of our target, so by -1 below we mean
    # to start our wall "to the left" of the 0th index
    # (we *don't* mean "the last index")
    floor_index = -1
    ceiling_index = len(nums)

    # if there isn't at least 1 index between floor and ceiling,
    # we've run out of guesses and the number must not be present
    while floor_index + 1 < ceiling_index:

        # find the index ~halfway between the floor and ceiling
        # we use integer division, so we'll never get a "half index"
        distance = ceiling_index - floor_index
        half_distance = distance / 2
        guess_index = floor_index + half_distance

        guess_value = nums[guess_index]

        if guess_value == target:
            return True

        if guess_value > target:

            # target is to the left, so move ceiling to the left
            ceiling_index = guess_index

        else:

            # target is to the right, so move floor to the right
            floor_index = guess_index

    return False
```

Careful: we can only use binary search if the input list is already sorted. to find second_movie_length in O(\lg{n})O(
lgn) time instead of O(n)O(n) time. But sorting would cost O(nlg(n))O(nlg(n)), and we can do even better than that.

Could we check for the existence of our second_movie_length in constant time?

What data structure gives us convenient constant-time lookups?

A set!

So we could throw all of our movie_lengths into a set first, in O(n)O(n) time. Then we could loop through our possible
first_movie_lengths and replace our inner loop with a simple check in our set. This'll give us O(n)O(n) runtime overall!

Of course, we need to add some logic to make sure we're not showing users the same movie twice...

But first, we can tighten this up a bit. Instead of two sequential loops, can we do it all in one loop?
(Done carefully, this will give us protection from showing the same movie twice as well.)

We know users won't watch the same movie twice because we check movie_lengths_seen for matching_second_movie_length
before we've put first_movie_length in it!

Complexity O(n)O(n) time, and O(n)O(n) space. Note while optimizing runtime we added a bit of space cost.

Bonus What if we wanted the movie lengths to sum to something close to the flight length (say, within 20 minutes)? What
if we wanted to fill the flight length as nicely as possible with any number of movies (not just 2)? What if we knew
that movie_lengths was sorted? Could we save some space and/or time? What We Learned The trick was to use a set to
access our movies by length, in O(1)O(1) time.

Using hash-based data structures, like dictionaries or sets, is so common in coding challenge solutions, it should
always be your first thought. Always ask yourself, right from the start: "Can I save time by using a dictionary?"

[Reference](https://www.interviewcake.com/question/python/inflight-entertainment?utm_source=weekly_email&utm_campaign=weekly_email&utm_medium=email)