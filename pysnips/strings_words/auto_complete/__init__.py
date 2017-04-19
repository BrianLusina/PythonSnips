def autocomplete(input_, dictionary):
    """
    Check if all the letters in the input are alphabetic, remove all letters in input that are not alphabetic
    :param input_: word 'user' is typing
    :param dictionary: dictionary to evaluate
    :return: list of possible matches based on first characters of word, restrict result to 5 matches
    :rtype list
    """
    res = []
    new_input = "".join([let for let in input_ if let.isalpha()])

    for word in dictionary:
        if word.startswith(new_input) or word.startswith(new_input.title()):
            res.append(word)
    return res[0:5]
