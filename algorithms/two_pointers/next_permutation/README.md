# Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending
order).

The replacement must be in place and use only constant extra memory.

## Constraints

- 1 <= `nums.length` <= 100
- 0 <= `nums[i]` <= 100


```
Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
```

```
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
```

```
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
```

```
Example 4:

Input: nums = [1]
Output: [1]
```

## Solution

The problem asks us to find the next permutation of a given array of numbers. This is the next “dictionary order” 
(lexicographical) arrangement of the same numbers. We can solve this problem using a two pointers (or more accurately, 
a “two-index”) approach, as it allows us to efficiently find the two critical positions in the array that need to be 
changed.

We use one pointer (or index) to find the “pivot” element we need to increase, and a second pointer to find the 
“successor” element to swap it with. This targeted, two-index approach enables us to perform the minimal change required,
which is crucial for finding the next permutation and satisfying the in-place, constant-memory constraints. To find the 
next smallest permutation that is larger than the current one, we need to make the smallest possible increase. This is 
done by modifying the “least significant” part of the array (the right-hand side) first. To do this, we make the 
smallest possible increase to the number, working from right to left:

1. **Find the pivot**: We scan from the right to find the first element (pivot) that is smaller than its right neighbor. 
   This is the element we will increase.

2. **Find the successor**: We scan from the right again to find the smallest element (successor) that is larger than the 
   pivot.

3. **Swap**: We swap the pivot and the successor.

4. **Reverse the suffix**: We reverse the part of the array to the right of the pivot’s original position. This ensures 
   the new suffix is in its smallest possible order (ascending). This single reverse operation also cleverly handles 
   both possible scenarios:
   - **Case 1 (pivot is found)**: The suffix (from i+1 onward) was previously in descending order. Reversing it sorts it
     into ascending order. This makes the new permutation as small as possible, ensuring it’s the immediate next one.
   - **Case 2 (no pivot is found)**: If the array were already in its largest order (e.g., [3,2,1]), the first loop 
     would finish with i=−1. This final step will then reverse from i+1 (which is index 0) to the end, correctly 
     transforming the entire array into its smallest possible order (e.g., .[1,2,3]).

Here’s a step-by-step breakdown of the code:

1. We initialize an index i to the second last element of nums. 
2. Next, we iterate backward starting from i to find the “pivot”. This is the rightmost element that can be changed to 
   increase the permutation’s size. 
3. Then, we check if a pivot is actually found (i.e., i is greater than or equal to 0). 
   - If a pivot is found, we initialize a second index, j, to the last element of nums. 
   - Then, we iterate backward from j to find the “successor”. This is the smallest possible number in the suffix that 
     we can swap with the pivot. 
   - Once the “successor” is found, we swap the pivot nums[i] with its successor nums[j]. This guarantees the new 
     permutation is larger than the original.
4. Finally, we reverse the portion of the array that comes after the pivot’s original index i (i.e., from index i + 1 
   to the end).

### Time Complexity

The time complexity of this solution is O(n), because in the worst-case scenario, we perform a single pass to find the 
pivot, another single pass to find the element to swap, and a final pass to reverse a part of the array.

### Space Complexity

The solution’s space complexity is O(1), as the permutation is done in-place, and only a constant amount of extra memory
is used for variables.