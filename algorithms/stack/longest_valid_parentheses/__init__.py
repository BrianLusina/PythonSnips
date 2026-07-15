def longest_valid_parentheses(s: str) -> int:
    """
    Return the length of the longest valid parentheses substring.

    >>> longest_valid_parentheses("(()")
    2
    >>> longest_valid_parentheses(")()())")
    4
    >>> longest_valid_parentheses("")
    0
    """
    # Stack to store indexes. We initialize it with -1 to serve as a
    # sentinel value. This handles the edge case of a valid substring
    # starting from index 0, allowing us to calculate its length correctly.
    stack = [-1]
    # Variable to store the maximum length of valid parentheses found so far.
    max_length = 0

    for index, char in enumerate(s):
        # If the character is an opening parenthesis, push its index onto the stack. It represents a potential start of
        # a valid sequence
        if char == "(":
            stack.append(index)
        elif char == ")":
            stack.pop()
            # iF the stack is now empty, it means the current ')' has no matching '('. We push the current index to act
            # as a new base or starting point for the next potential valid substring
            if len(stack) == 0:
                stack.append(index)
            else:
                # If the stack is not empty, a valid pair was just formed
                # The new top of the stack holds the index of the character just 'before' the start of the current valid
                # substring. The length is the difference between the current index and that 'base' index
                current_length = index - stack[len(stack) - 1]

                # Update the overall maximum length if the current one is greater
                max_length = max(max_length, current_length)

    return max_length
