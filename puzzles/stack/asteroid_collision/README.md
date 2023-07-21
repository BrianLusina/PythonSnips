# Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning
right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both
are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

## Solution

### Approach: Stack

We have NNN asteroids, each represented by an integer. The absolute value represents the size, and the sign (positive or
negative) of the integer represents the direction the asteroid is moving; all stones are moving at the same speed. These
asteroids can collide, and if they do, the smaller one explodes and vanishes. If both asteroids are of the same size,
then both will explode. We need to return the final state of asteroids after all collisions.

The first important thing to find out is when two asteroids will collide. Two stones moving in the same direction can
never collide. Hence it's tempting to assume that whenever two asteroids are moving in opposite directions, they will
collide.

Now, if we iterate over asteroids from left to right, then each asteroid moving left will collide with asteroids that
came before it that are moving right. If the current stone is smaller than the one we saw earlier, it will explode, and
the collision chain will stop there. On the other hand, if it's bigger, it will keep moving toward the left and might
collide further with other asteroids we saw earlier that are moving toward the right. Hence, the observation here is
that each stone might keep colliding with asteroids on its left until it collides with a bigger asteroid and explodes.
This requirement could be fulfilled by the stack data structure; if we keep asteroids in the stack, then for each
asteroid, the collision chain can be executed by checking the top of the stack and popping if an asteroid should be
destroyed.

### Complexity Analysis

Here, N is the number of asteroids in the list.

#### Time complexity: O(N).

We iterate over each asteroid in the list, and for each asteroid, we might iterate over the asteroids we have in the
stack and keep popping until they explode. The important point is that each asteroid can be added and removed from the
stack only once. Therefore, each asteroid can be processed only twice, first when we iterate over it and then again
while popping it from the stack. Therefore, the total time complexity is equal to O(N).

#### Space complexity: O(N).

The only space required is for the stack; the maximum number of asteroids that could be there in the stack is N when
there is no asteroid collision. The final list that we return is used to store the output, which is
generally not considered part of space complexity. Hence, the total space complexity equals O(N).

## Related Topics

- Array
- Stack
- Simulation
