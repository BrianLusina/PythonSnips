# lst[1::2] = [__mul__(x, 2) for x in lst[1::2]]


def double_every_other(lst):
    lst[1::2] = [x * 2 for x in lst[1::2]]
    return lst
