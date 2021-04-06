def consecutive(arr):
    """
    Sort the string from min to max
    get the range from the min to max number and store in a variable,
    return the difference of the 2 lists
    :param arr: The array to evaluate
    :return: the number of consecutive numbers needed
    """
    if len(arr) == 0 or len(arr) == 1:
        return 0
    s = sorted(arr)
    m = range(s[0], s[len(s) - 1] + 1)
    return len(m) - len(s)

# or
# return max(arr) - min(arr) + 1 - len(arr) if arr else 0
