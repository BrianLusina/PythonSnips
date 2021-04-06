def comp(array1, array2):
    """

    :param array1: list with numbes to evaluate
    :param array2: squares of array1
    :rtype bool
    :return: if squares of array1 are in array2
    """
    if array1 is None or array2 is None:
        return True
    if len(array1) == 0 or len(array2) == 0:
        return True
    m = [x ** 2 for x in array1]
