from typing import List


def min_length_stack(s: str) -> int:
    stack: List[str] = []

    for char in s:
        # If the stack is empty
        if len(stack) == 0:
            # Add the current character to the stack and continue to the next character
            stack.append(char)
            continue
        # If the current character is B and the top of the stack is A
        if char == "B" and stack[-1] == "A":
            # Pop off the character from the stack
            stack.pop()
        # If the current character is D and the top of the stack is C
        elif char == "D" and stack[-1] == "C":
            # Pop off the character from the top of the stack
            stack.pop()
        else:
            # otherwise, push the current character to the stack
            stack.append(char)
    return len(stack)


def min_length_string_replace(s: str) -> int:
    while "AB" in s or "CD" in s:
        if "AB" in s:
            s = s.replace("AB", "")
        elif "CD" in s:
            s = s.replace("CD", "")

    return len(s)


def min_length_in_place_manipulation(s: str) -> int:
    char_list = list(s)
    write_ptr = 0

    for read_ptr in range(len(s)):
        # Write the current character to the current write position
        char_list[write_ptr] = char_list[read_ptr]

        # Check if we have a valid pattern to remove
        if (
            write_ptr > 0
            and char_list[write_ptr - 1] in "AC"
            and ord(char_list[write_ptr]) == ord(char_list[write_ptr - 1]) + 1
        ):
            write_ptr -= 1
        else:
            write_ptr += 1  # No match, so move the write pointer forward

    return write_ptr
