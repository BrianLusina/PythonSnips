# Divide Chocolate

You have a chocolate bar made up of several chunks, and each chunk has a certain sweetness, given in an array called 
sweetness. You want to share the chocolate with k friends. To do this, you’ll make k cuts to divide the bar into k + 1 
parts. Each part will consist of consecutive chunks.

Being a kind person, you’ll take the piece with the minimum total sweetness and give the other pieces to your friends.

Your task is to find the maximum total sweetness of the piece you will receive if you cut the chocolate bar optimally.

## Constraints

- 0 <= k < sweetness.length <= 10^3
- 1 <= sweetness[i] <= 10^3

## Solution

As we have a chocolate bar made of several chunks, each with its own sweetness value, dividing the chocolate evenly 
won’t ensure that we get the chocolate part with the maximum possible minimum sweetness. The next natural thought for 
solving this problem is to try to cut the chocolate in different ways and find out the one that gives the desired result.
But it becomes very inefficient when the chocolate bar is long. There are just too many possible combinations of where 
to cut, and checking each one would take too much time.

So, instead of guessing exactly where to cut, we flip the problem and ask: What is the largest minimum sweetness we can 
guarantee for ourselves if we divide the chocolate bar into k + 1 pieces?

The idea is to guess a sweetness value, called S , and check if it’s possible to cut the chocolate into k + 1 parts, 
where each part has at least S sweetness. Go through the chocolate chunks one by one, adding their sweetness. When the 
total reaches S or more, count it as one piece and start a new one. If it’s possible to make at least k + 1 such pieces, 
then S is a good guess. If not, the guess is too high and should be lowered. For example, if S=5 , keep adding chunks 
until the total is 5 or more. Count that as one piece and reset the total to 0 . Repeat this through the whole chocolate 
bar.

The sweetness value is guessed using the binary search. The lower bound is 1, and the upper bound is the total sweetness 
divided by (k + 1), as no single piece can have more than that if the chocolate is divided evenly. Start by guessing the
middle value. If it allows at least k + 1 valid parts, try a higher value. Otherwise, try a lower one. This quickly 
narrows down the largest sweetness that can be guaranteed.

Now, let’s look at the algorithm steps below:

1. Initialize the binary search range:
   - Set low (the smallest possible minimum sweetness for a piece) as 1, because sweetness values are at least 1.
   - Set high (the largest possible minimum sweetness) as the total sweetness divided evenly among k + 1 people, using 
     the formula sum(sweetness) // (k + 1). This is the best possible sweetness each person could get if the chocolate 
     were divided perfectly.

2. Start the binary search, and while low is less than or equal to high, do the following:
   - Calculate the mid-point value, mid = (low + high) // 2. This represents the current guess for the maximum minimum 
     sweetness we might be able to give to each person.
   - Use the helper function canDivide(sweetness, k, mid) to check if dividing the chocolate into at least k + 1 pieces 
     is possible, where each piece has a total sweetness of at least mid. The helper works by summing chunks and counting
     how many full pieces it can form with at least mid sweetness. 
   - If it’s possible to divide into k + 1 or more such pieces:
     - That means we can afford to aim for even higher sweetness per person. So we move the lower bound up: low = mid + 1.
     - We also store mid as a potential result, result.

3. If it’s not possible to make enough pieces:
   - Then our guess mid was too high, so we reduce the upper bound: high = mid - 1.

4. After the binary search ends, return the last valid result, which is the maximum possible minimum sweetness we can 
   guarantee for each person.

### Time Complexity

Let n be the total number of chunks in the chocolate bar, and S be the upper bound for our binary‐search range, i.e., 
the sum of values in the sweetness list divided by k + 1. Each call to the helper function scans the entire sweetness 
array once, taking O(n) time. The binary search is performed over the integer range [1…S], which takes O(log S) iterations. 
Therefore, the overall time complexity of this solution is O(n×logS).

### Space Complexity

We only use a fixed number of extra variables, and no additional arrays or data structures. Therefore the space complexity
is O(1).
