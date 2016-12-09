def manipulate_data(array):
    """
    First checks if the input is a list outputs an error if it is not
    Loops through the array to find positive numbers, counts each occurrence
    if a negative number is found sums the negs counter variable
    Only lists allowed
    :param array: List of integers
    :return: count of positive numbers and sum of negative numbers as a list
    """
    pos, neg = 0, 0
    if not isinstance(array, list):
        return "Only lists allowed"
    for num in array:
        if num >= 0:
            pos += 1
        else:
            neg += num
    return [pos, neg]
