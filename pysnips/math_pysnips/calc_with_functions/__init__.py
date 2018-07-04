def zero(operation=None):
    if operation is None:
        return 0
    return int(eval(f"0 {operation}"))


def one(operation=None):
    if operation is None:
        return 1
    return int(eval(f"1 {operation}"))


def two(operation=None):
    if operation is None:
        return 2
    return int(eval(f"2 {operation}"))


def three(operation=None):
    if operation is None:
        return 3
    return int(eval(f"3 {operation}"))


def four(operation=None):
    if operation is None:
        return 4
    return int(eval(f"4 {operation}"))


def five(operation=None):
    if operation is None:
        return 5
    return int(eval(f"5 {operation}"))


def six(operation=None):
    if operation is None:
        return 6
    return int(eval(f"6 {operation}"))


def seven(operation=None):
    if operation is None:
        return 7
    return int(eval(f"7 {operation}"))


def eight(operation=None):
    if operation is None:
        return 8
    return int(eval(f"8 {operation}"))


def nine(operation=None):
    if operation is None:
        return 9
    return int(eval(f"9 {operation}"))


def plus(number):
    return f"+ {number}"


def minus(number):
    return f"- {number}"


def times(number):
    return f"* {number}"


def divided_by(number):
    return f"/ {number}"
