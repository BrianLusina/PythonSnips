There is a horizontal row of cubes. The length of each cube is given. You need to create a new vertical pile of cubes.
The new pile should follow these directions: if `cubei` is on top of `cubej` then .
`sideLengthj >= sideLengthi`

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print "Yes" if it is
possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.

Input Format

The first line contains a single integer , the number of test cases. For each test case, there are lines. The first line
of each test case contains , the number of cubes. The second line contains space separated integers, denoting the
sideLengths of each cube in that order.

Constraints

```plain
1 <= T <= 5
1 <= n <= 10
1 <= sideLength <= 2^31
``` 

Output Format

For each test case, output a single line containing either "Yes" or "No" without the quotes.

Sample Input

```
2
6
4 3 2 1 3 4
3
1 3 2
```

Sample Output

```plain
Yes
No
```

Explanation

In the first test case, pick in this order: left - , right - , left - , right - , left - , right - . In the second test
case, no order gives an appropriate arrangement of vertical cubes. will always come after either 1 or 2.