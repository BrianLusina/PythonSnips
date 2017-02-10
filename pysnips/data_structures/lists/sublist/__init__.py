SUBLIST, SUPERLIST, EQUAL, UNEQUAL = 0, 1, 2, 3


def check_lists(list1, list2):
    if list1 == list2:
        return EQUAL
    if contains(list1, list2):
        return SUPERLIST
    if contains(list2, list1):
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
        for i in range(len(l2)):
            if l1[x + i] != l2[i]:
                break
        else:
            return True
    return False
