from math import sqrt, ceil


def encode(message):
    """
    Encodes the message
    :param message: String message to be encoded
    :return: encoded message
    :rtype str
    """
    normalize_text = normalize(message)
    square_size = get_square_size(normalize_text)
    c, res = 0, []
    while c < square_size:
        for segment in get_segments(normalize_text):
            if c < len(segment):
                res.append(segment[c])
        if c < square_size - 1:
            res.append(" ")
        c += 1

    return "".join(res)


def get_segments(normalize_text):
    """
    Gets the chunks/segments of the normalized plain text in rows and columns
    chars: the length of the normalized text, :type int
    square_size: the size of the rectangle from the chars :type int
    :param normalize_text: the normalized text
    :return: the chunks of the normalized text for encoding
    :rtype list
    """
    chars = len(normalize_text)
    square_size = get_square_size(normalize_text)

    indx, chunks = 0, []

    # get the text segments
    while indx < chars:
        if indx + square_size < chars:
            chunks.append(normalize_text[indx: indx + square_size])
        else:
            chunks.append(normalize_text[indx:])
        indx += square_size
    return chunks


def normalize(msg):
    """
    Normalizes the plain text removing all invalid characters and spaces
    :param msg: Plain text to be normalized
    :return: the normalized message without invalid chars
    """
    return "".join([let.lower() for let in msg if let.isalpha() or let.isdigit()])


def get_square_size(message):
    """
    Evaluates the square size of the normalized text
    :param message:
    :return: the size of the rectangle
     :rtype int
    """
    chars = len(message)
    return ceil(sqrt(chars))
