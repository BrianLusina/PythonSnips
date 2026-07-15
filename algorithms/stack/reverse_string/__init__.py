from typing import List

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


def reverse_string_char_array(s: List[str]) -> None:
    """
    Reverses a character array in place using two-pointer technique.

    Reference: https://leetcode.com/problems/reverse-string/

    Complexity:
    Where n is the length of the input list
    Time: O(n), each character is visited at most once
    Space: O(1), only two pointers used, no extra data structures

    Args:
        s (List[str]): character array to reverse in place
    Returns:
        None: modifies the input list in place
    """
    if not s or len(s) == 1:
        return

    # Initialize two pointers: left at start, right at end
    left = 0
    right = len(s) - 1

    # Swap characters while left is before right
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
