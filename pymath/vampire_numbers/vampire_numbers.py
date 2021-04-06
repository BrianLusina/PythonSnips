def vampire_test(x, y):
    product = x * y
    if len(str(x) + str(y)) != len(str(product)):
        return False

    for i in str(x) + str(y):
        if i in str(product):
            return True
        else:
            return False
