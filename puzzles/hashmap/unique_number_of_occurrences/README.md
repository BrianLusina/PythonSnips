# Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false
otherwise.

```plain

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true 
```

## Solution

### Approach: HashMap & HashSet

#### Intuition

If we have the frequencies of all elements, we can put them in a hash set. If the size of the hash set is equal to the
number of elements, it implies that the frequencies are unique. Hence, we will find the frequencies of all elements in a
hash map and then put them in a hash set.

#### Algorithm

Algorithm
Store the frequencies of elements in the array arr in the hash map freq.
Iterate over the hash map freq and insert the frequencies of all unique elements of array arr in the hash set freqSet.
Return true if the size of hash set freqSet is equal to the size of hash map freq, otherwise return false.

#### Complexity Analysis

Here, `N` is the size of array arr.

- Time complexity: `O(N)`.

  We iterate over the array arr to find the frequency and store them in the hash map freq. Then, we insert these
  frequencies in the hash set freqSet, which has the insertion complexity of O(1). Hence, the total time
  complexity is equal to O(N).


- Space complexity: `O(N)`.

  We are storing the N frequencies in the hash map freq that takes O(1) space for each element. We also store
  the frequency count in the hash set. Therefore, the total space complexity is equal to O(N).

## Related Topics

- Array
- Hash Table
