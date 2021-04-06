A crack team of love scientists from OkEros (a hot new dating site) have devised a way to represent dating profiles as
rectangles on a two-dimensional plane.

They need help writing an algorithm to find the intersection of two users' love rectangles. They suspect finding that
intersection is the key to a matching algorithm so powerful it will cause an immediate acquisition by Google or Facebook
or Obama or something.

![](https://www.interviewcake.com/images/svgs/rectangular_love__it_must_be_love.svg?bust=143)

Write a function to find the rectangular intersection of two given love rectangles.

As with the example above, love rectangles are always "straight" and never "diagonal." More rigorously: each side is
parallel with either the x-axis or the y-axis.

They are defined as dictionaries ↴ like this :

```python

my_rectangle = {

    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 5,

    # width and height
    'width': 10,
    'height': 4,

}
```

Your output rectangle should use this format as well.

Let's break this problem into subproblems. How can we divide this problem into smaller parts?

We could look at the two rectangles’ "horizontal overlap" or "x overlap" separately from their "vertical overlap" or "y
overlap."

Lets start with a helper function find_x_overlap().

Since we’re only working with the x dimension, we can treat the two rectangles' widths as ranges on a 1-dimensional
number line.

What are the possible cases for how these ranges might overlap or not overlap? Draw out some examples!

There are four relevant cases:

1) The ranges partially overlap:

![](https://www.interviewcake.com/images/svgs/rectangular_love__partially_overlap.svg?bust=143)

Two horizontal parallel lines. The right half of the top line overlaps the left half of the bottom line.

2) One range is completely contained in the other:

![](https://www.interviewcake.com/images/svgs/rectangular_love__completely_contained.svg?bust=143)

Two horizontal parallel lines. The bottom line is longer than the top line and extends farther out to the left and
right.

3) The ranges don't overlap:

![](https://www.interviewcake.com/images/svgs/rectangular_love__dont_overlap.svg?bust=143)

Two horizontal parallel lines. The right end of the bottom line is to the left of the left end of the top line.

4) The ranges "touch" at a single point:

![](https://www.interviewcake.com/images/svgs/rectangular_love__touch_at_single_point.svg?bust=143)

Two horizontal parallel lines. The right end of the bottom line is directly below the left end of the top line.

Let's start with the first 2 cases. How do we compute the overlapping range?

One of our ranges starts "further to the right" than the other. We don't know ahead of time which one it is, but we can
check the starting points of each range to see which one has the highest_start_point. That highest_start_point is always
the left-hand side of the overlap, if there is one.

Not convinced? Draw some examples!

Similarly, the right-hand side of our overlap is always the lowest_end_point. That may or may not be the end point of
the same input range that had the highest_start_point—compare cases (1) and (2).

This gives us our x overlap! So we can handle cases (1) and (2). How do we know when there is no overlap?

If highest_start_point > lowest_end_point, the two rectangles do not overlap.

But be careful—is it just greater than or is it greater than or equal to?

It depends how we want to handle case (4) above.

If we use greater than, we treat case (4) as an overlap. This means we could end up returning a rectangle with zero
width, which ... may or may not be what we're looking for. You could make an argument either way.

Let's say a rectangle with zero width (or zero height) isn't a rectangle at all, so we should treat that case as "no
intersection."

Here's one way to do it:

```python
def find_x_overlap(x1, width1, x2, width2):

    # find the highest ("rightmost") start point and lowest ("leftmost") end point
    highest_start_point = max(x1, x2)
    lowest_end_point = min(x1 + width1, x2 + width2)

    # return null overlap if there is no overlap
    if highest_start_point >= lowest_end_point: 
        return None, None

    # compute the overlap width
    overlap_width = lowest_end_point - highest_start_point

    return highest_start_point, overlap_width
```

Can we just make one find_range_overlap() function that can handle x overlap and y overlap?

Yes! We simply use more general parameter names:

```python
def find_range_overlap(point1, length1, point2, length2):

    # find the highest start point and lowest end point.
    # the highest ("rightmost" or "upmost") start point is
    # the start point of the overlap.
    # the lowest end point is the end point of the overlap.
    highest_start_point = max(point1, point2)
    lowest_end_point = min(point1 + length1, point2 + length2)

    # return null overlap if there is no overlap
    if highest_start_point >= lowest_end_point:
        return None, None

    # compute the overlap length
    overlap_length = lowest_end_point - highest_start_point

    return highest_start_point, overlap_length
```

We've solved our subproblem of finding the x and y overlaps! Now we just need to put the results together

Complexity O(1)O(1) time and O(1)O(1) space.

Bonus What if we had a list of rectangles and wanted to find all the rectangular overlaps between all possible pairs of
two rectangles within the list? Note that we'd be returning a list of rectangles.

What if we had a list of rectangles and wanted to find the overlap between all of them, if there was one? Note that we'd
be returning a single rectangle.

What We Learned This is an interesting one because the hard part isn't the time or space optimization—it's getting
something that works and is readable.

For problems like this, I often see candidates who can describe the strategy at a high level but trip over themselves
when they get into the details.

Don't let it happen to you. To keep your thoughts clear and avoid bugs, take time to:

Think up and draw out all the possible cases. Like we did with the ways ranges can overlap. Use very specific and
descriptive variable names.