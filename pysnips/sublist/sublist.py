SUBLIST, SUPERLIST, EQUAL, UNEQUAL = 0, 1, 2, 3


def check_lists(lst_a, lst_b):
    if lst_a == lst_b:
        return EQUAL
    if contains(lst_a, lst_b):
        return SUPERLIST
    if contains(lst_b, lst_a):
        return SUBLIST
    return UNEQUAL


def contains(l1, l2):
    if not l2:
        return True
    if len(l2) > len(l1):
        return False
    for x in range(len(l1) - len(l2) + 1):
        if l1[x] != l2[0]:
            continue
        for y in range(len(l2)):
            if l1[x + y] != l2[y]:
                break
        else:
            return True
    return False
