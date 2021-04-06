import string

GROUP_SIZE = 5
ALPHA = string.ascii_lowercase
CIPHER = string.ascii_lowercase[::-1]


def decode(str_to_decode):
    return do_filter_join(str_to_decode)


def encode(str_to_encode):
    return grouper(do_filter_join(str_to_encode))


def do_filter_join(m):
    """
    Filters a string and joins the result
    :param m:
    :return:
    """
    return "".join(cipher(x) for x in filter_string(m).lower())


def filter_string(filtr):
    """
    Filter function to remove invalid characters
    :param filtr:
    :return:
    """
    return "".join(x for x in filtr if x.isalpha())


def cipher(char):
    """
    Checks if the character is in the cipher an returns its cipher
    :param char:
    :return:
    """
    indx = ALPHA.index(char)
    return CIPHER[indx] if indx >= 0 else char


def grouper(txt_to_group):
    """
    groups the words into five letters
    :param txt_to_group:
    :return:
    """
    count, grouped = 0, []
    while count < len(txt_to_group):
        if count + GROUP_SIZE <= len(txt_to_group):
            grouped.append(txt_to_group[count:count + GROUP_SIZE])
        else:
            grouped.append(txt_to_group[count:])
        count += GROUP_SIZE
    return " ".join(grouped)
