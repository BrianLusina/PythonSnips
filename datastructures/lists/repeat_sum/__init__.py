def repeat_sum(list_lists):
    """
    pseudo code
    create an empty list to store the unpacked lists
    perform a for loop to iterate through the list of lists and another to unpack them into the concat lists
    count the occurrences of each number in the concat and add to the counter list
    sum the counter list
    """
    concat = []
    for x in list_lists:
        for i in set(x):
            concat.append(i)
    counter = set([y for y in concat if concat.count(y) >= 2])
    return sum(list(counter))
