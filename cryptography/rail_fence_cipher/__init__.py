from itertools import cycle, chain


def fence_pattern(rail, size):
    """
    Creates a fence pattern for th encoding of messages
    This is done by creating a zig zag pattern using cycle and chain
    chain will 'chain' the rail and the decreasing rail range to create 1 long iterable
    cycle will produce this chain until it is exhausted
    :param rail: The rail length
    :param size: Size of the rows on the rail
    :return: The fence pattern to use
    """
    zig = cycle(chain(range(rail), range(rail - 2, 0, -1)))
    return zip(zig, range(size))


def encode(message, rail):
    """
    Encodes the message by taking the 2nd element in the sorted list of tuples
    uses this second element to get the ith character in the message and adding it to a list
    This list is joined to create a newly encoded message
    :param message:The string message to be encoded
    :param rail: :type int The height of the rail
    :return: Encoded message
    :rtype :type str
    """
    fence = fence_pattern(rail=rail, size=len(message))
    return "".join(message[i] for _, i in sorted(fence))


def decode(encrypt, rail):
    """
    Creates fence pattern and zips each character in the encrypted message to each tupe in the sorted
    fence pattern
    Sorts the encrypted message by the second element of the fence pattern
    Joins the characters to form the decrypted message
    :param encrypt: the string message to decrypt
    :param rail: The height of the rail
    :return: The decrypted message
    :rtype: :type str
    """
    fence = fence_pattern(rail=rail, size=len(encrypt))
    fence_msg = zip(encrypt, sorted(fence))
    return "".join(char for char, _ in sorted(fence_msg, key=lambda item: item[1][1]))
