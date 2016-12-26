def count(paren):
    stack = []
    push_chars, pop_chars = "<({[", ">)}]"
    for c in paren:
        if c in push_chars:
            stack.append(c)
        elif c in pop_chars:
            if not len(stack):
                return False
            else:
                stack_top = stack.pop()
                balancing_bracket = push_chars[pop_chars.index(c)]
                if stack_top != balancing_bracket:
                    return False
        else:
            return False
    return not len(stack)


def is_valid(code):
    openers_to_closers_map = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    openers = frozenset(openers_to_closers_map.keys())
    closers = frozenset(openers_to_closers_map.values())

    openers_stack = []

    for char in code:
        if char in openers:
            openers_stack.append(char)
        elif char in closers:
            # check if stack is empty
            if not openers_stack:
                return False
            else:
                # remove the opener and store in variable
                last_unclosed_opener = openers_stack.pop()

                # if this closer doesn't correspond to the most recently
                # seen unclosed opener, short-circuit, returning false
                if not openers_to_closers_map[last_unclosed_opener] == char:
                    return False

    return openers_stack == []
