# Dot Product of Two Sparse Vectors

You need to implement a class called SparseVector that efficiently handles sparse vectors (vectors with mostly zero
values) and computes their dot product.

The class should support:

Constructor SparseVector(nums): Takes a list of integers nums and initializes the sparse vector
Method dotProduct(vec): Computes the dot product between the current sparse vector instance and another sparse vector vec
A sparse vector is a vector containing mostly zeros. Instead of storing all elements including zeros, you should store
it efficiently by only keeping track of non-zero values.

The dot product of two vectors is calculated by multiplying corresponding elements and summing the results. For example,
if vector A = [1, 0, 3] and vector B = [2, 0, 4], their dot product would be 1*2 + 0*0 + 3*4 = 14.

The solution uses a hash map (dictionary) to store only non-zero elements, where:

- Keys represent the indices of non-zero elements
- Values represent the actual non-zero values at those indices

When computing the dot product:

- The code identifies which vector has fewer non-zero elements for optimization
- It iterates through the smaller hash map
- For each element, it checks if the same index exists in the other vector's hash map
- If both vectors have non-zero values at the same index, their product is added to the result

Follow-up consideration: The problem asks what happens if only one vector is sparse. The current implementation handles
this efficiently by always iterating through the smaller hash map, minimizing the number of lookups needed.

## Topics

- Design
- Array
- Hash Table
- Two Pointers

## Constraints

- n == `nums1.length` == `nums2.length`
- 1 <= n <= 10^3
- 0 <= `nums1[i]`, `nums2[i]` <= 100

## Intuition

When dealing with sparse vectors that contain mostly zeros, storing all elements wastes memory. Consider a vector with
10,000 elements where only 10 are non-zero - storing all 10,000 values is inefficient.

The key insight is that when computing a dot product, zeros don't contribute to the final sum. If either element in a
pair is zero, their product is zero. Therefore, we only need to care about positions where both vectors have non-zero
values.

This leads us to think about storing only the non-zero elements. A hash map is perfect for this because:

We can store only index-value pairs where the value is non-zero
Looking up whether a specific index exists is O(1) on average
The space complexity becomes proportional to the number of non-zero elements rather than the total vector length
For the dot product calculation, we need to find indices where both vectors have non-zero values. Instead of checking
all indices, we can iterate through one hash map and check if each index exists in the other.

The optimization of iterating through the smaller hash map comes from minimizing the number of lookups. If vector A has
5 non-zero elements and vector B has 100 non-zero elements, it's more efficient to iterate through A's 5 elements and
look them up in B, rather than iterating through B's 100 elements and looking them up in A. This reduces the operation
from 100 lookups to just 5 lookups.

The get(i, 0) method elegantly handles the case where an index doesn't exist in the other vector - it returns 0, which
correctly contributes nothing to the dot product sum.

## Time And Space Complexity

**Time Complexity**: O(n) for initialization and O(min(m, k)) for dot product operation, where n is the length of the input
array, m and k are the number of non-zero elements in the two sparse vectors respectively.

- **Initialization (__init__)**: The dictionary comprehension iterates through all n elements of the input array to
  identify and store non-zero values, resulting in O(n) time complexity.

- **Dot Product (dotProduct)**: The method first compares the sizes of the two dictionaries and swaps them if needed
  (O(1)). Then it iterates through the smaller dictionary, performing a lookup in the larger dictionary for each element.
  Since dictionary lookup is O(1) on average, and we iterate through min(m, k) elements, the time complexity is
  `O(min(m, k))`.

**Space Complexity**: O(m) where m is the number of non-zero elements in the sparse vector.

- The hash map stores only the non-zero elements and their indices. In the worst case where all elements are non-zero,
  this would be O(n), but for truly sparse vectors where m << n, the space complexity is `O(m)`.
- The dotProduct method uses O(1) additional space as it only creates references to existing dictionaries and computes
  the sum on the fly without storing intermediate results.

> Note: O(n) for both complexities is possible which represents the worst-case scenario where all elements in the vector
are non-zero. For sparse vectors with few non-zero elements, the actual complexity can be much better than O(n).
