Design a stack that supports push, pop, top, and retrieving the maximum element in constant time.

Implement the MaxStack class:

MaxStack() initializes the stack object.
void push(val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMax() retrieves the minimum element in the stack.
 

Example 1:

Input
["MaxStack","push","push","push","getMax","pop","top","getMax"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MaxStack minStack = new MaxStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMax(); // return 0
minStack.pop();
minStack.top();    // return 0
minStack.getMax(); // return 0