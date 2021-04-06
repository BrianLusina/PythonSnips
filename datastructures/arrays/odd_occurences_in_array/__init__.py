def odd_occurences_in_array(a):
    """
    Finds the odd number of occurences of an element in an array.
    XOR of all elements gives us odd occurring element. 
    Note that XOR of two elements is 0 if both elements are same and XOR of a number x with 0 is x
    :param a
    """
    result = 0

    for number in a:
        result = result ^ number
    return result
