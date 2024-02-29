from typing import List


def candy(ratings: List[int]) -> int:
    """
    Uses a Greedy Algorithm with a Two-Pass Method.
    A Greedy Algorithm makes choices that seem optimal at the moment. For this problem, we use a two-pass greedy
    approach to make sure each child gets the minimum number of candies that still satisfy the conditions.

    Intuition

    1. Initialize Candies Array:
        We start by creating a candies array of the same length as the ratings array and initialize all its values to 1.
         This is the base case and ensures that every child will receive at least one candy, satisfying the first
         condition.

    2. Forward Pass: Left to Right

        Now, we iterate through the ratings array from the beginning to the end. For each child (except the first), we
        compare their rating with the one to the left. If it's higher, we update the candies array for that child to be
        one more than the child on the left. This takes care of the second condition but only accounts for the child's
        left neighbor.

    3. Backward Pass: Right to Left
        After the forward pass, we loop through the array again but in the reverse direction. This time, we compare
        each child's rating with the child to their right. If the rating is higher, we need to make sure the child has
        more candies than the right neighbor. So, we update the candies array for that child to be the maximum between
        its current number of candies and one more than the right neighbor's candies. This ensures that both neighboring
         conditions are checked and satisfied.

    4. Summing it All Up

        Finally, we sum up all the values in the candies array. This will give us the minimum total number of candies
        that need to be distributed to satisfy both conditions.

    Time and Space Complexity
    - Time Complexity: O(n), because we make two passes through the array.
    - Space Complexity: O(n), for storing the candies array.

    Args:
        ratings (List): list of ratings per child

    Return:
        (int): minimum candies to distribute

    """
    n = len(ratings)
    candies = [1] * n

    for idx in range(1, n):
        if ratings[idx] > ratings[idx - 1]:
            candies[idx] = candies[idx - 1] + 1

    for idx in range(n - 2, -1, -1):
        if ratings[idx] > ratings[idx + 1]:
            candies[idx] = max(candies[idx], candies[idx + 1] + 1)

    return sum(candies)
