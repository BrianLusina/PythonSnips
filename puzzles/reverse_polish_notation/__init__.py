from typing import List


def eval_rpn(tokens: List[str]) -> int:
    stack: List[int] = []

    for c in tokens:
        if c == "+":
            n1, n2 = stack.pop(), stack.pop()
            res = n1 + n2
            stack.append(res)
        elif c == "-":
            n1, n2 = stack.pop(), stack.pop()
            res = n2 - n1
            stack.append(res)
        elif c == "*":
            n1, n2 = stack.pop(), stack.pop()
            res = n1 * n2
            stack.append(res)
        elif c == "/":
            n1, n2 = stack.pop(), stack.pop()
            res = n2 / n1
            stack.append(int(res))
        else:
            stack.append(int(c))

    return stack[0]
