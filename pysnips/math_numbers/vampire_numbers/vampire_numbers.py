from itertools import permutations


def vampire_test(x, y):
    product = x * y
    if len(str(x) + str(y)) != len(str(product)):
        return False

    for i in str(x) + str(y):
        if i in str(x * y):
            return True
        else:
            return False
