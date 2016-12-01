def count(paren):
    stack = []
    pushChars, popChars = "<({[", ">)}]"
    for c in paren:
        if c in pushChars:
            stack.append(c)
        elif c in popChars:
            if not len(stack):
                return False
            else:
                stackTop = stack.pop()
                balancingBracket = pushChars[popChars.index(c)]
                if stackTop != balancingBracket:
                    return False
        else:
            return False
    return not len(stack)


def is_valid(code):
    openers_to_closers_map = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }

    openers = frozenset(openers_to_closers_map.keys())
    closers = frozenset(openers_to_closers_map.values())

    openers_stack = []

    for char in code:
        if char in openers:
            openers_stack.append(char)
        elif char in closers:
            if not openers_stack:
                return False
            else:
                last_unclosed_opener = openers_stack.pop()

                # if this closer doesn't correspond to the most recently
                # seen unclosed opener, short-circuit, returning false
                if not openers_to_closers_map[last_unclosed_opener] == char:
                    return False

    return openers_stack == []