def digit_sum(n):
    # function to sum all the digits of a number
    # convert the number into a string
    stringConvert = str(n)
    return sum([int(i) for i in stringConvert])





"""that takes in a list and removes elements of the list that are the same."""
def remove_duplicates(myList):
    return list(set(myList))
