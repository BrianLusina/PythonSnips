# Number of Flowers in Full Bloom

You are given a 0-indexed 2D integer array, flowers, where each element flowers[i]=[starti ,endi] represents the time 
interval during which the ith flower is in full bloom (inclusive).

You are also given a 0-indexed integer array, people, of size n, where people[i] denotes the time at which the ith person
arrives to view the flowers. For each person, determine how many flowers are in full bloom at their arrival time. 
Return an integer array, ans, of length n, where ans[i] is the number of blooming flowers when the ith person arrives.

## Constraints

- 1 <= flowers.length <= 10^3
- `flowers[i].length` == 2
- 1 <= starti <= endi <= 10^4
- 1 <= people.length <= 10^3
- 1 <= people[i] <= 10^4

### Solution

The core intuition behind this solution is to avoid directly simulating flower blooming across all possible time values,
which would be inefficient. Instead, we transform the problem into one of counting intervals using binary search. The 
challenge is to determine a person’s arrival time. The difference between these two counts gives the number of flowers 
in bloom at that moment.

To achieve this, the solution separates the flowers’ intervals into two lists: one for start times and one for end times.
The key trick is that the end times are stored as endi+1 instead of endi. This ensures that when a person arrives at 
exactly endi, the flower is still counted as blooming. With both lists sorted, we can use binary search to quickly 
determine counts for any arrival time.

Let’s break down the key steps of the solution:

1. Initialize the starts and ends arrays for storing start and end times, respectively.
2. Iterate over each flower interval [starti, endi].
   - Add starti to the starts list.
   - Add endi+1 to the ends list.
3. Sort both lists to ensure that binary search can efficiently count the number of flowers that started or ended before
   a given arrival time.
4. Create an ans list of size n to store the answer for each person.
5. Iterate over people array and for each person’s arrival time, perform two binary searches:
   - On starts, find how many flowers began blooming at or before the arrival time.
   - On ends, find how many flowers had already finished blooming before the arrival time.
   - Store the difference between the counts in the ans array.
6. After completing the iteration, return the ans array as the output.

Binary Search implementation details:
- The binarySearch function is a modified version of the standard algorithm. 
- It returns the index of the first element greater than the target (upper bound). 
- This effectively gives the count of values ≤ target.

### Time Complexity

- Creating the starts and ends arrays of length n takes O(n) time.
- Sorting both arrays costs O(nlogn).
- Next, for each of the m people, we perform two binary searches on these arrays, each taking O(logn) time. This 
contributes O(mlogn) in total.

So, the overall time complexity is O(nlogn+mlogn), which simplifies to O((n+m)logn).

### Space Complexity

The space complexity is O(n) because the solution stores all n flowers’ start and end times in separate lists (starts 
and ends). So, the overall space complexity is O(n).
