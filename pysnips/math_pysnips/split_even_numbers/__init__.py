# todo: work on this to fix splitting even numbers
def split_all_even_numbers(numbers, way):
    """
    Splits even numbers found in the array into odd numbers based on the way provided:
    the ways provided, if the even number provided is 8
        0 -> Split into two odd numbers, that are closest to each other.
        (e.g.: 8 -> 3,5)
        1 -> Split into two odd numbers, that are most far from each other.
        (e.g.: 8 -> 1,7)
        2 -> All new odd numbers from the splitting should be equal and the maximum possible number.
        (e.g.: 8 -> 1, 1, 1, 1, 1, 1, 1, 1)
        3 -> Split into 1s.
        (e.g.: 8 -> 1, 1, 1, 1, 1, 1, 1, 1)
    :param numbers: the array of numbers
    :param way: way to split the even numbers found
    :return: a new list with only odd numbers
    :rtype:list
    """
    # create a copy of the numbers array
    result = numbers[:]

    # if the way is 0, split the even number into the odd numbers that are closet to each other
    # loop through the numbers array and check for even numbers
    # use a range from 1 up to the even number (excluding it) and check only for odd numbers
    if way == 0:
        for num in result:
            # if the number is even
            if num % 2 == 0:
                print("Even num: ", num)

                # get the position of the even number
                even_pos = result.index(num)
                print("Index position of even number", even_pos)

                # create a range for only odd numbers in the range upto the number
                rnge, indx = list(range(1, num, 2)), 0
                print("Odd numbers in the range: ", rnge)
                for _ in rnge:
                    print("Sum of two odds: ", sum(rnge[indx: indx + 2]))
                    # if the sum of the 2 closest odd numbers sums to the odd number
                    if rnge[indx] + rnge[indx + 2] == num:
                        # replace the num with the 2 odd numbers
                        result[even_pos: even_pos + 1] = rnge[indx: indx + 2]
                        break
                    indx += 1
    elif way == 1:
        pass
    elif way == 2:
        pass
    elif way == 3:
        pass

    return result


# [1, 5, 5, 1, 3]
print(split_all_even_numbers([1, 10, 1, 3], 0))
