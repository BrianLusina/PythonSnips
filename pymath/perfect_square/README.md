# Perfect Squares

Given an integer, n, return the least number of perfect square numbers that sum to n.

> A perfect square is an integer that is the square of an integer. In other words, it is an integer that is the result of 
> multiplying a whole integer by itself. For example, 1, 4, 9 and 16 are perfect squares, but 3, 5, and 11 are not.

## Constraints 

- 1 <= `n` < 10^3

## Solution

One of the first solutions that comes to mind is to keep subtracting perfect squares (like 9, 16, 25, …) until we reach 
zero, counting how many times it takes. But that greedy idea doesn’t always find the smallest number of squares. For 
example, trying the biggest square each time may miss a better combination. Instead, this problem has a clever 
mathematical shortcut that utilizes some deep results from number theory, specifically the Four-Square theorem and the 
Three-Square theorem.

The Four-Square theorem says every number can be written as the sum of at most four perfect squares. So, the answer will
always be one of 1, 2, 3, or 4. The Three-Square theorem tells us that some numbers can’t be expressed as the sum of 
three squares, and these are exactly the numbers that look like 4^a(8b+7) That means, if a number (after dividing out 
all factors of 4) is of the form 8b+7, then it needs four squares. Using these ideas, we can build a simple check-and-decide
algorithm instead of trying all combinations. First, we remove all factors of 4 from the number, because multiplying or 
dividing by 4 doesn’t change how many squares are needed; it just scales them. Then, we check the remainder when divided 
by 8. If it’s 7, the number must have four squares. Otherwise, we check if it’s already a perfect square (then the answer
is 1). If not, we test if it can be written as the sum of two perfect squares (then the answer is 2). If none of those 
conditions are true, we know from the theorems that it must be 3. So, rather than testing every combination, this 
approach uses mathematical reasoning to narrow the answer step by step, making it very fast and elegant.

Let’s look at the algorithm steps:

- Keep dividing n by 4 while it is divisible by 4. This simplifies the number without changing the answer. If a number 
  is built from perfect squares, then four times that number is built from the same squares, just doubled. So, dividing 
  by 4 doesn’t affect how many squares we need; it only makes the number smaller to work with.
- If the reduced number has a remainder of 7 when divided by 8 (n % 8 == 7), return 4 immediately, because it must need
  four squares.
- Check if n is a perfect square itself. If yes, return 1.
  - Try to write n as a sum of two perfect squares. Iterate over all possible i from 1 to √n, and check if n - i² is also 
  a perfect square. If such a pair exists, return 2.
- If none of the above conditions are true, return 3. By elimination, the number can be expressed as the sum of three 
  squares.

### Time Complexity

We check if the number can be decomposed into the sum of two squares, which takes O(sqrt(n)) iterations. In the remaining 
cases, we perform the check in constant time.

### Space Complexity

The algorithm consumes a constant space, regardless of the size of the input number, so O(1).
