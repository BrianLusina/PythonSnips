# Find Duplicate in Array

Problem Description

Given a read-only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than
O(n) space and traversing the stream sequentially O(1) times.
If there are multiple possible answers ( like in the sample case ), output any one, if there is no duplicate, output -1

Example Input:

```plain
Input 1:
A = [3, 4, 1, 4, 2]
Input 2:
A = [1, 2, 3]
Input 3:
A = [3, 4, 1, 4, 1]

Example Output
Output 1:
4
Output 2:
-1
Output 3:
1
```

Example Explanation:

```plain
Explanation 1:
4 repeats itself in the array [3, 4, 1, 4, 2]
Explanation 2:
No number repeats itself in the array [1, 2, 3]
Explanation 3:
1 and 4 repeats itself in the array [3, 4, 1, 4, 1], we can return 1 or 4
```

> Note: You cannot modify the given array nums. You have to solve the problem using only constant extra space.

## Solution

This solution involves two key steps: identifying the cycle and locating the entry point of this identified cycle, which
represents the duplicate number in the array.

The fast and slow pointers technique detects such cycles efficiently, where one pointer takes one step at a time and the
other advances by two steps. Initially pointing at the start of the array, the position of each pointer for the next step
is determined by the current value they are pointing to. If a pointer points to the value 5 at index 0, its next position
will be index 5. As the pointers traverse the array, both will eventually catch up because there’s a cycle. This is
because, in the noncyclic part, the distance between the pointers increases by one index in each iteration. However, once
both pointers enter the cyclic part, the fast pointer starts closing the gap on the slow pointer, decreasing the distance
by one index each iteration until they meet.

Once the duplicate number is confirmed, we reset one of the pointers (usually the slow pointer) to index 0 while the
other stays at the position where the pointers met. Then, both pointers move one step at a time until they meet again.
With this positioning and pace of pointers, pointers are guaranteed to meet at the cycle’s starting point, corresponding
to the duplicate number.

Now, let’s look at the detailed workflow of the solution:

For this problem, the duplicate number will create a cycle in the nums array. The cycle in the nums array helps identify
the duplicate number.

To find the cycle, we’ll move in the nums array using the `f(x)=nums[x]`, where x is the index of the array. This
function constructs the following sequence to move:

      x, nums[x], nums[nums[x]], nums[nums[nums[x]]], ...

In the sequence above, every new element is an element in nums present at the index of the previous element.

Let’s say we have an array,[2, 3, 1, 3]. We’ll start with `x=nums[0]`, which is 2, present at the 0th index of the array
and then move to nums[x], which is 1, present at the 2nd index. Since we found 1 at the 2nd index, we’ll move to the 1st,
and so on. This example shows that if we’re given an array of length n+1, with values in the range [1, n], we can use this
traversal technique to visit all the locations in the array.

The following example illustrates this traversal:

![Solution 1](./images/solutions/find_duplicate_solution_1.png)
![Solution 2](./images/solutions/find_duplicate_solution_2.png)
![Solution 3](./images/solutions/find_duplicate_solution_3.png)
![Solution 4](./images/solutions/find_duplicate_solution_4.png)
![Solution 5](./images/solutions/find_duplicate_solution_5.png)
![Solution 6](./images/solutions/find_duplicate_solution_6.png)
![Solution 7](./images/solutions/find_duplicate_solution_7.png)
![Solution 8](./images/solutions/find_duplicate_solution_8.png)
![Solution 9](./images/solutions/find_duplicate_solution_9.png)
![Solution 10](./images/solutions/find_duplicate_solution_10.png)
![Solution 11](./images/solutions/find_duplicate_solution_11.png)

Now, let's dive deep into how our two parts of the solution work.

In the first part, the slow pointer moves once, while the fast pointer moves twice as fast as the slow pointer until
both of the pointers meet each other. Since the fast pointer is moving twice as fast as the slow pointer, it will be the
first one to enter and move around the cycle. At some point after the slow pointer also enters and moves in the cycle,
the fast pointer will meet the slow pointer. This will be the intersection point.

> Note: The intersection point of the two pointers is, in the general case, not the entry point of the cycle.

![Solution 12](./images/solutions/find_duplicate_solution_12.png)
![Solution 13](./images/solutions/find_duplicate_solution_13.png)
![Solution 14](./images/solutions/find_duplicate_solution_14.png)
![Solution 15](./images/solutions/find_duplicate_solution_15.png)
![Solution 16](./images/solutions/find_duplicate_solution_16.png)
![Solution 17](./images/solutions/find_duplicate_solution_17.png)
![Solution 18](./images/solutions/find_duplicate_solution_18.png)
![Solution 19](./images/solutions/find_duplicate_solution_19.png)
![Solution 20](./images/solutions/find_duplicate_solution_20.png)

In part two, we’ll start moving again in the cycle, but this time, we’ll slow down the fast pointer so that it moves
with the same speed as the slow pointer.

Let’s look at the journeys of the two pointers in part two:

- The slow pointer will start from the 0th position.
- The fast pointer will start from the intersection point.
- After a certain number of steps, let’s call it F, the slow pointer meets the fast pointer. This is the ending point
  for both pointers.
- This common ending position will be the entry point of the cycle.

Let’s look at the visual presentation of the second part of our solution:

![Solution 21](./images/solutions/find_duplicate_solution_21.png)
![Solution 22](./images/solutions/find_duplicate_solution_22.png)
![Solution 23](./images/solutions/find_duplicate_solution_23.png)

Now, let’s try to understand how it is that our solution is able to always locate the entry point of the cycle.

Let’s return to the example we just discussed, using this graphical representation:

![Solution 24](./images/solutions/find_duplicate_solution_24.png)

- 7 is the intersection point where the slow and fast pointers will meet.
- 8 is the entry point of the cycle, which is our duplicate number.

The fast pointer is traversing two times faster than the slow pointer. This can be represented by the following equation:

> dfast = 2dslow ———(1)

Here, d represents the number of elements traversed.

Let’s look at the following diagram to see the steps taken by the slow and fast pointers from the starting point to the
intersection point:

![Solution 25](./images/solutions/find_duplicate_solution_25.png)

> A list with a cycle

In the diagram above:

- Green represents the entry point of the cycle.
- Blue represents the intersection point.
- Yellow represents the starting point.
- F represents the steps taken from the starting point to the entry point.
- a represents the steps taken to reach the intersection point from the entry point.
- C represents the cycle length, in terms of the number of steps taken to go once around the cycle.

With this setup in mind, let’s see the distance traveled by the slow and fast pointers. The slow pointer travels F steps
from the starting point to the entry point of the cycle and then takes a steps from the entry point to the intersection
point of the cycle, that is, the point where both pointers intersect. So, we can express the distance traveled by the
slow pointer in the form of this equation:

dslow = F+a ——— (2)

In the time it takes the slow pointer to travel F+a steps, the fast pointer, since it’s traveling twice as fast as the
slow pointer, will have also traveled around the cycle at least once. So, we can say the fast pointer, first, travels F
steps from the starting point to the entry point of the cycle, then travels at least a cycle, and at the end travels a
steps from the entry point to the intersection point of the cycle. Now, we can express the distance traveled by the fast
pointer as the following equation:

dfast = F+C+a ——— (3)

Recall eq. (1):

dfast = 2dslow ——— (1)

If we substitute the equivalent expression of dslow given in eq. (2) and the equivalent expression of dfast given in eq. 
(3) into eq. (1), we get:

F + C + a = 2(F + a)

Let’s simplify this equation:

F + C + a = 2F + 2a
C = F + a

Therefore, the distance from the starting point to the intersection point, F+a, equals C.

We can also re-arrange this equality as follows:

F=C−a

Let’s consult our diagram again:

![Solution 26](./images/solutions/find_duplicate_solution_26.png)

As we can see, C−a is, in fact, the distance from the intersection point back to the entry point. This illustrates why,
when we move one pointer forward, starting at the intersection point, and another pointer from the starting point, the
point where they meet is the entry point of the cycle.

> Note: The proof above does not consider the case where F is longer than the length of the cycle. In this situation,
> it’s possible that the fast pointer will go around the cycle more than once. To express this more general case, we can
> say that the distance covered by the fast pointer from the entry point to the intersection point is: F+nC+a, where n
> is a positive integer. As a result, our substitution will take this form: F + nC + a = 2(F+a), which simplifies to 
> nC=F+a, that is: F = nC − a. This simply means that after going around the cycle n times, the fast pointer will still
> be a steps behind the entry point of the cycle.

### Time Complexity

The time complexity of the algorithm is O(n), where n is the length of nums. This is because, in each part of the
solution, the slow pointer traverses nums just once.

### Space Complexity

The algorithm takes O(1) space complexity, since we only used constant space to store the fast and slow pointers.
