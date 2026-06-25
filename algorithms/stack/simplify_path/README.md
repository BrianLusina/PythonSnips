# Simplify Path

You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to
transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

- A single period '.' represents the current directory.
- A double period '..' represents the previous/parent directory.
- Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
- Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For
example, '...' and '....' are valid directory or file names.

The simplified canonical path should follow these rules:

- The path must start with a single slash '/'.
- Directories within the path must be separated by exactly one slash '/'.
- The path must not end with a slash '/', unless it is the root directory.
- The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.

Return the simplified canonical path.

## Examples

Example 1:

```text
Input: path = "/home/"

Output: "/home"

Explanation:

The trailing slash should be removed.
```

Example 2:
```text
Input: path = "/home//foo/"

Output: "/home/foo"

Explanation:

Multiple consecutive slashes are replaced by a single one.
```

Example 3:

```text
Input: path = "/home/user/Documents/../Pictures"

Output: "/home/user/Pictures"

Explanation:

A double period ".." refers to the directory up a level (the parent directory).
```

Example 4:

```text
Input: path = "/../"

Output: "/"

Explanation:

Going one level up from the root directory is not possible.
```

Example 5:
```text
Input: path = "/.../a/../b/c/../d/./"

Output: "/.../b/d"

Explanation:

"..." is a valid name for a directory in this problem.
```

## Constraints

- 1 <= path.length <= 3000
- path consists of English letters, digits, period '.', slash '/' or '_'.
- path is a valid absolute Unix path.

## Topics

- String
- Stack

## Solution

Think of navigating through directories like walking through rooms in a building. When you encounter a directory name,
you enter that room (go deeper). When you see '..', you go back to the previous room (go up one level). When you see '.',
you stay in the same room (no movement).

The key insight is that we need to keep track of our current path as we process each component. A stack is perfect for
this because:

- Directory navigation is inherently stack-like: When you enter a directory, you're adding to your path (push). When you
  go back with '..', you're removing the last directory you entered (pop).
- We only care about the final state: We don't need to preserve the original path structure - we just need to know where
  we end up after all the navigation commands.
- Sequential processing: We can process the path from left to right, making decisions about each component independently
  based on simple rules.

By splitting the path on '/', we get individual components that we can evaluate:

- Empty strings (from consecutive slashes) and '.' don't change our position
- '..' means go back (pop from stack if possible)
- Everything else is a real directory name to enter (push to stack)

After processing all components, the stack contains exactly the directories in our final path, in order from root to
destination. Joining them with '/' and adding a leading '/' gives us the canonical path.

This approach naturally handles edge cases like trying to go above root (stack is empty, so pop does nothing) and
multiple consecutive slashes (they create empty strings that we skip).

Step-by-step implementation:

- Split the path into components: Use path.split('/') to break the path into individual directory names. This
  automatically handles multiple consecutive slashes by creating empty strings between them.

- Initialize an empty stack: stk = [] will store the valid directory names in our final path. 
- Process each component: Iterate through each substring s from the split operation:
  - Skip empty strings and current directory: If s is empty (from consecutive slashes) or equals '.', continue to the
    next iteration
  - Handle parent directory: If s == '..':
    - Check if the stack is not empty before popping (we can't go above root)
    - If stk has elements, call stk.pop() to remove the last directory
  - Handle regular directories: For any other string (including '...', '....', etc.):
    - Push it onto the stack with stk.append(s)
- Build the final path: After processing all components:
  - Join all elements in the stack with '/' separator: '/'.join(stk)
  - Add a leading '/' to ensure the path starts with root: '/' + '/'.join(stk)
  - This automatically handles the root directory case (empty stack returns '/')

### Time and Space Complexity

#### Time Complexity: O(n), where n is the length of the path string.

The algorithm performs the following operations:

- path.split('/'): This operation traverses the entire string once to split it by '/', which takes O(n) time.
- The for loop iterates through each component produced by the split operation. In the worst case, there could be O(n)
  components (though typically much fewer).
- Inside the loop, each operation (append, pop, string comparison) takes O(1) time for each component.
- '/'.join(stk): This operation takes O(m) time where m is the total length of all strings in the stack, which is
  bounded by O(n) since these strings came from the original path.

Overall, the time complexity is O(n) + O(n) = O(n).

#### Space Complexity: O(n), where n is the length of the path string.

The space usage includes:

- The stk list: In the worst case, if the path contains no '..' or '.' and all valid directory names, the stack could
  store all components from the path, using up to O(n) space.
- The result of path.split('/'): This creates a list of substrings that together can be at most O(n) characters.
- The final string created by '/' + '/'.join(stk): This creates a new string of length at most O(n).

Therefore, the total space complexity is O(n).
