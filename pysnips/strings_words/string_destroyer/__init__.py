from string import ascii_lowercase


def destroyer(input_sets):
    """
    takes in a tuple with 1 or more sets of characters and replaces the alphabet with letters that are in the sets
    First gets the candidates of the alphabets and gets the letters to knock out into a list

    :param input_sets:
    :return: string of letters with the letters in the input sets having been replaced with _
    :rtype: str
    """
    letters_to_knock = []
    candidates = " ".join([let for let in ascii_lowercase])
    result = ""
    for sets in input_sets:
        for char in sets:
            letters_to_knock.append(char)

    for let in candidates:
        if let in letters_to_knock:
            result += "_"
        else:
            result += let

    return result


# alternative
def destroyer_2(input_sets):
    from string import ascii_lowercase as alphabet
    return " ".join(c if c not in set.union(*input_sets) else "_" for c in alphabet)
