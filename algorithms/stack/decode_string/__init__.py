def decode_string(s: str) -> str:
    stack, result, num = [], "", 0

    for char in s:
        # If the character is a digit, update num to accumulate the multi-digit number
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == "[":
            # When encountering '[', push num and result onto the stack
            stack.append(result)
            stack.append(num)
            # Reset num and result for the new segment inside the brackets
            result = ""
            num = 0
        elif char == "]":
            # When encountering ']', pop the last string and count from the stack
            popped_num = stack.pop()
            popped_str = stack.pop()
            # Repeat the result string popped_num times and append it to the popped string
            result = popped_str + popped_num * result
        else:
            # For regular characters, append them to the result string
            result += char

    # Return the fully decoded string after processing all characters
    return result


def decode_string_2(s: str) -> str:
    # Initialize two stacks: one for numbers (repeat counts) and one for strings
    count_stack = []
    string_stack = []

    # Initialize an empty string to hold the current decoded segment
    current = ""
    # Initialize k to accumulate multi-digit numbers for repeat counts
    k = 0

    # Loop through each character in the input string s
    for char in s:
        if char.isdigit():
            # If the character is a digit, update k to accumulate the multi-digit number
            k = 10 * k + int(char)
        elif char == "[":
            # When encountering '[', push k onto the count stack and current onto the string stack
            count_stack.append(k)
            string_stack.append(current)
            # Reset k and current for the new segment inside the brackets
            k = 0
            current = ""
        elif char == "]":
            # When encountering ']', pop the last string and count from the stacks
            popped_string = string_stack.pop()
            num = count_stack.pop()
            # Repeat the current string num times and append it to the popped string
            current = popped_string + current * num
        else:
            # For regular characters, append them to the current string
            current += char

    # Return the fully decoded string after processing all characters
    return current
