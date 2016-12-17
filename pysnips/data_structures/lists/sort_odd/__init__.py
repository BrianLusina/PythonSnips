def sort_array(source_array):
    """
    loop through array checking for odd and even numbers,
    if number is odd, look for th next odd number and compare them, if the previous is greater than the next, swap them
    leave the even numbers in place
    :param source_array:Array of integers to sort
    :return: the sorted array
    """
    if len(source_array) == 0:
        return source_array
    for num in range(len(source_array), 0, -1):
        for x in range(num):
            if source_array[x] % 2 != 0 and source_array[x + 1] % 2 != 0:
                if source_array[x] > source_array[x+1]:
                    curr = source_array[x]
                    source_array[x] = source_array[x + 1]
                    source_array[x + 1] = curr
                    print("After swapping", curr, source_array[x])

    return source_array

