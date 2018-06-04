import operator


def zero(operation=None):
    if operation is None:
        return 0


def one(operation=None):
    if operation is None:
        return 1
    return 1


def two(operation=None):
    if operation is None:
        return 2
    return 2


def three(operation=None):
    if operation is None:
        return 3
    return 3


def four(operation=None):
    if operation is None:
        return 4
    return 4


def five(operation=None):
    if operation is None:
        return 5
    return 5


def six(operation=None):
    if operation is None:
        return 6
    return 6


def seven(operation=None):
    if operation is None:
        return 7
    return 7


def eight(operation=None):
    if operation is None:
        return 8
    return 8


def nine(operation=None):
    if operation is None:
        return 9
    return 9


def plus(number):
    return operator.add(number())


def minus(number):
    pass


def times(number):
    pass


def divided_by(number):
    pass
