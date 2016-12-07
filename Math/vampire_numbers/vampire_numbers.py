
def vampire_test(x, y):
    for i in str(x)+str(y):
        if i in str(x * y):
            return True
        else:
            return False

