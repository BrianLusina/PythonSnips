# Max Points You Can Obtain From Cards

Given an array of integers representing card values, write a function to calculate the maximum score you can achieve by
picking exactly k cards.

You must pick cards in order from either end. You can take some cards from the beginning, then switch to taking cards
from the end, but you cannot skip cards or pick from the middle.

For example, with k = 3:

- Take the first 3 cards: valid
- Take the last 3 cards: valid
- Take the first card, then the last 2 cards: valid
- Take the first 2 cards, then the last card: valid
- Take card at index 0, skip some, then take card at index 5: not valid (skipping cards)

## Constraints

- 1 <= k <= cards.length
- 1 <= `cards.length` <= 10^5
- 1 <= `cards[i]` <= 10^4

## Examples

Example 1:
```text
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize
your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
```

Example 2:
```text
Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
```

Example 3:
```text
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
```

## Topics

- Array
- Sliding Window
- Prefix Sum

## Solutions

When you pick k cards from either end of the array, you're actually leaving behind n - k consecutive cards in the middle
that you didn't pick.

For example, with cards = [2,11,4,5,3,9,2] and k = 3:

![Solution 1](./images/solutions/max_points_from_cards_solution_1.png)

Every possible way to pick 3 cards from the ends corresponds to a different window of 4 cards (n - k = 7 - 3 = 4) in the
middle that we're NOT picking.

### Why This Matters

Since we know the total sum of all cards, we can calculate:

Sum of picked cards = Total sum - Sum of unpicked cards

So to maximize the sum of picked cards, we need to minimize the sum of unpicked cards.

This transforms the problem: instead of trying all combinations of picking from ends, we find the minimum sum of any
window of size n - k.

![Solution 2](./images/solutions/max_points_from_cards_solution_2.png)

### Algorithm

Use a fixed-length sliding window of size n - k to find the minimum sum of any consecutive n - k cards. For each window
position, calculate total - window_sum to get the corresponding score, and track the maximum.

![Solution 3](./images/solutions/max_points_from_cards_solution_3.png)
![Solution 4](./images/solutions/max_points_from_cards_solution_4.png)
![Solution 5](./images/solutions/max_points_from_cards_solution_5.png)
![Solution 6](./images/solutions/max_points_from_cards_solution_6.png)
![Solution 7](./images/solutions/max_points_from_cards_solution_7.png)
![Solution 8](./images/solutions/max_points_from_cards_solution_8.png)
![Solution 9](./images/solutions/max_points_from_cards_solution_9.png)
![Solution 10](./images/solutions/max_points_from_cards_solution_10.png)
![Solution 11](./images/solutions/max_points_from_cards_solution_11.png)
![Solution 12](./images/solutions/max_points_from_cards_solution_12.png)
![Solution 13](./images/solutions/max_points_from_cards_solution_13.png)
![Solution 14](./images/solutions/max_points_from_cards_solution_14.png)
![Solution 15](./images/solutions/max_points_from_cards_solution_15.png)
![Solution 16](./images/solutions/max_points_from_cards_solution_16.png)
![Solution 17](./images/solutions/max_points_from_cards_solution_17.png)
![Solution 18](./images/solutions/max_points_from_cards_solution_18.png)
![Solution 19](./images/solutions/max_points_from_cards_solution_19.png)
![Solution 20](./images/solutions/max_points_from_cards_solution_20.png)
![Solution 21](./images/solutions/max_points_from_cards_solution_21.png)
