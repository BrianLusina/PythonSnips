# Flatten Nested List Iterator

You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also
be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

- NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
- int next() Returns the next integer in the nested list.
- boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.

Your code will be tested with the following pseudocode:

> initialize iterator with nestedList
> res = []
> while iterator.hasNext()
    append iterator.next() to the end of res
> return res

If `res` matches the expected flattened list, then your code will be judged as correct.

## Examples

Example 1:

```text
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be:
[1,1,2,1,1].
```

Example 2:
```text
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be:
[1,4,6].
```

## Constraints

- 1 <= nestedList.length <= 500
- The values of the integers in the nested list is in the range [-10^6, 10^6].

## Topics

- Stack
- Tree
- Depth-First Search
- Design
- Queue
- Iterator

## Solution(s)

1. [Depth-First Search Approach](#depth-first-search-approach)
2. [Stack Approach](#stack-approach)

### Depth-first Search Approach

When we look at this nested list structure, we're essentially dealing with a tree where each node can either be a leaf
(integer) or a branch (nested list). The challenge is to visit every integer in the correct order, just like reading a
book - we read each word sequentially, even though the book has a hierarchical structure of chapters, sections, and
paragraphs.

The key insight is recognizing that we need to "flatten" this hierarchical structure into a linear sequence. Think of it
like unpacking nested boxes - we open the main box, and for each item inside, if it's another box, we open that too,
continuing until we find all the actual items (integers).

Since we need to access elements one by one through next() calls, we have two main strategies:

- Lazy evaluation: Only flatten elements when needed during next() or hasNext() calls
- Eager evaluation: Flatten everything upfront during initialization

The eager approach is simpler and more intuitive here. Why? Because:

- We're going to visit all elements anyway (the iterator will traverse the entire structure)
- Pre-flattening makes next() and hasNext() operations trivial - just array indexing
- We avoid the complexity of maintaining state about partially explored nested lists

The DFS pattern naturally fits this problem because it mirrors how we'd manually flatten the list: when we encounter a
nested list, we immediately dive into it, process all its contents, then continue with the next element at the current
level. This is exactly what DFS does - it goes as deep as possible before backtracking.

The recursive nature of DFS perfectly matches the recursive structure of nested lists. Each recursive call handles one
level of nesting, and the base case (finding an integer) is where we actually collect the values into our flattened
result.

#### Complexity Analysis

##### Time Complexity

- Constructor: `O(n)` where n is the total number of integers in the nested list structure. The DFS traversal visits
  each element exactly once, whether it's an integer or a nested list. For each integer element, we perform an `O(1)`
  append operation.
- next(): `O(1)` - Simply increments the index and returns the element at that position in the flattened list.
- hasNext(): `O(1) `- Just compares the current index with the length of the list.

##### Space Complexity

- `O(n + d)` where n is the total number of integers in the nested structure and d is the maximum depth of nesting.
  - `O(n)` for storing all integers in `self.flattened_list` list after flattening.
  - `O(d)` for the recursive call stack during DFS traversal, where d represents the maximum nesting depth.
  - In the worst case where the structure is deeply nested (like `[[[[...[[1]]...]]]`), the space complexity would be
    `O(n)` for both the storage and call stack combined.

Analysis: The approach flattens the entire nested structure upfront during initialization using DFS. This trades
initialization time for constant-time iteration operations. All integers are extracted and stored in a simple list,
making subsequent next() and hasNext() operations very efficient at O(1) each.

---

### Stack Approach

We’ll use a stack to solve this problem. The stack will be used to store the integer and list of integers on the iterator
object. We’ll push all the nested list data in the stack in reverse order in the constructor. The elements are pushed in
reverse order because the iterator is implemented using a stack. In order to process the nested list correctly, the
elements need to be accessed in the order they appear in the original nested list.

Here is how we implement the NestedIterator class methods to solve the above problem:

**Constructor**

1. The constructor initializes an empty stack of NestedInteger objects.
2. The constructor iterates through the input nestedList, starting from the last element to the first element
   (reverse order). It pushes each element onto the stack using stack.push().

**`hasNext()` method**

The hasNext() method checks if there is a next integer to return from the stack, iterating through nested lists if
necessary.

1. The top element of the stack is retrieved using stack.peek().
2. The top element is checked using the method top.isInteger():
   - If it is an integer, the method returns TRUE because the next element is an integer.
   - The top element must be a nested list if it is not an integer. In this case:
     - The top element is popped from the stack using stack.pop().
     - The list is retrieved using top.getList().
     - The elements of this nested list are pushed onto the stack in reverse order using stack.push(). This ensures that
       the first element of the nested list will be processed first.
3. If the stack is empty, the method returns FALSE.

**`next()` method**

The next() method returns the next integer from the stack.
1. The method calls hasNext() to check if more integers are available. If hasNext() returns true, the method pops the
   top element of the stack using stack.pop(), which will be an integer because hasNext() ensures that any nested lists
   are flattened and only integers remain in the stack.
2. If hasNext() returns false, the method returns 0.

#### Complexity Analysis

##### Time Complexity

Assume 
- n is the number of elements, 
- l is the number of nested lists, and 
- d is the maximum nesting depth (maximum number of lists inside each other).

**Constructor**: Since the constructor pushes all of the elements from the nested list into the stack, the total time
will be the size of that list. Therefore, the time complexity will be `O(n+l)`.

**Has Next ()**: This function will be called several times. During all of these calls, the function will iterate over
all the lists exactly once (the while loop) and process every integer exactly once. Thus, a total of `O(n+l)` effort is
spent. The iterator will be progressed for every integer in the nested list. Thus, there will be a total of `O(n)` calls.
Accordingly, the running time for one call to Has Next is `O((n+l)/n)=O(l/n)`.

Next (): This function calls the Has Next function every time. So, its complexity will be the same as that of the Has
Next function, that is, `O(l/n)`.

##### Space Complexity

The space complexity will be `O(n+l)`

In the worst-case scenario, whereby the outermost list contains 
n integers or l empty sub-lists, it will cost `O(n+l)` space. Other expensive cases occur when the nesting is very deep.
It’s useful to remember that d≤l (because each layer of nesting requires another list), but we don’t need to consider
this for our case.
