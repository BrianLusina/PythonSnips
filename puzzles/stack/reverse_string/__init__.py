from datastructures.stacks.dynamic import DynamicSizeStack as Stack


def reverse_string(text: str) -> str:
    """
    Reverses an input string using a stack data structure
    Complexity:
    Where n is the length of the input string
    Time: O(n), iterate through the whole string
    Space: O(n), a stack is used to store the characters in the input string.
    Args:
        text (str): string to reverse
    Return:
        str: reversed string
    """
    # initialize an empty stack
    stack = Stack()

    # push all the characters onto the stack
    for char in text:
        stack.push(char)

    # initialize an empty string which will be the result
    reversed_string = ""

    # iterate over all the items in the stack popping of items from the top of the stack and adding them to the result
    # string.
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string
