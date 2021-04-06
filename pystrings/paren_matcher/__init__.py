def closing_paren(sentence, open_paren_index):
    """

    :param: sentence the sentence to search through
    :param: open_paren_index, index of the opening parenthesis
    """
    open_nested_count = 0
    position = open_paren_index + 1

    while position <= len(sentence):
        char = sentence[position]
        if char == "(":
            open_nested_count += 1
        elif char == ")":
            if open_nested_count == 0:
                return position
            else:
                open_nested_count -= 1
        position += 1

    raise Exception("No closing parenthesis :(")
