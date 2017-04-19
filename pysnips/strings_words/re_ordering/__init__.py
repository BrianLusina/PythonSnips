def re_ordering(s):
    """
    Split the string into a list,
    loop through the list, then loop through each word checking if any letter is capital
    if so, obtain the index of the word insert it at the beginning and remove it from old position
    """
    k, reorder = s.split(), ""
    for x in k:
        for y in x:
            if y.isupper():
                ind = k.index(x)
                k.insert(0, k.pop(ind))
    return " ".join(k)
