class Functions(object):
    """
    Class of random functions to be called by iterator
    """

    # returns the double of a number
    @staticmethod
    def get_double(number):
        return number * 2


def create_iterator(func, n):
    c = 0
    while c < n:
        func *= func
        c += 1
    return func


print(create_iterator(Functions.get_double(5), 3))
