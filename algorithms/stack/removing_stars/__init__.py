def remove_stars_with_stack(word: str) -> str:
    stack = []

    for char in word:
        if char == "*":
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)
