def check_brackets_1(code):
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


# another version to the solution
def check_brackets_2(string):
    counterparts = {')': '(', '}': '{', ']': '['}

    stack = []
    for char in string:
        if char in counterparts.values():
            stack.append(char)
        elif char in counterparts:
            if not stack:
                return False
            if stack.pop() != counterparts[char]:
                return False
    return not stack


def check_brackets_3(paren):
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
