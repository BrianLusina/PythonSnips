# Happy Number

Write an algorithm to determine if a number n is a happy number.

We use the following process to check if a given number is a happy number:

- Starting with the given number n, replace the number with the sum of the squares of its digits. 
- Repeat the process until:
  - The number equals 1, which will depict that the given number n is a happy number.
  - The number enters a cycle, which will depict that the given number n is not a happy number.
 
Return TRUE if n is a happy number, and FALSE if not.

## Examples

### Sample Example 1

![Sample Example 1.1](example_1_1.png)
![Sample Example 1.2](example_1_2.png)
![Sample Example 1.3](example_1_3.png)

### Sample Example 2

![Sample Example 2.1](example_2_1.png)
![Sample Example 2.2](example_2_2.png)
![Sample Example 2.3](example_2_3.png)

## Solution Example

Below shows an example using Floyd's Cycle Detection Algorithm or Tortoise and Hare algorithm to detect a cycle
for the number 2.

![Solution Example 1](solution_example_1.png)
![Solution Example 2](solution_example_2.png)
![Solution Example 3](solution_example_3.png)
![Solution Example 4](solution_example_4.png)
![Solution Example 5](solution_example_5.png)
![Solution Example 6](solution_example_6.png)
![Solution Example 7](solution_example_7.png)
![Solution Example 8](solution_example_8.png)
