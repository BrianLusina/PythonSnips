def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


def memoize(func):
    """
    Custom memo function that will cache results of the function
    This will take in the func argument and create an inner function that will perform the calculations.
    This will check the cache for the result and if the arguments do not exist, the function is called and new result
    is created and stored
    :param: func Function to memoize
    :return: function
    :rtype: func
    """
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func
