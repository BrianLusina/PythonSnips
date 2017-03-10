def xbonacci(signature, n):
    """
    Calculates the xbonacci sequence of a given signature. This signature of elements is a list of numbers
    :param signature: initial list of elements
    :param n: the number of elements to add to get the next number in the sequence
    :return: a list of numbers not greater in length than n
    :rtype: list
    """
    # result list to store output of operation and counter variable to determine when to stop calculation
    result, c = signature[:], 0

    # while the counter variable is less than n, sum the elements of the signature to get the next output
    while c < n:
        next_num = sum(result[c:])
        result.append(next_num)
        c += 1
        if len(result) == n:
            break
    return result


# print(xbonacci([1, 0, 0, 0, 0, 0, 1], 10))
# [1, 0, 0, 0, 0, 0, 1, 2, 3, 6])

