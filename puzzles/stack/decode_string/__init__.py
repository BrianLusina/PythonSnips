def decode_string(s: str) -> str:
    stack, result, num = [], "", 0

    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == "[":
            stack.append(result)
            stack.append(num)
            result = ""
            num = 0
        elif char == "]":
            p_num = stack.pop()
            p_str = stack.pop()
            result = p_str + p_num * result
        else:
            result += char

    return result
