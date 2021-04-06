EIGHTBITMASK = 0x80
SEVENBITSMASK = 0x7f


def encode_single(num):
    """
    Encodes a single number
    :param num: number to encode
    :return: list of bytes
    """
    bytes_result = [num & SEVENBITSMASK]
    num >>= 7

    while num > 0:
        bytes_result.append(num & SEVENBITSMASK | EIGHTBITMASK)
        num >> 7

    return bytes_result[::-1]


def encode(numbers):
    """
    Encodes a list of numbers in HEX 
    :param numbers: list of numbers e.g [0X0, 0X40]
    :return: list of encoded numbers following VLQ
    """
    return sum((encode_single(n) for n in numbers), [])


def decode(bytes_):
    """
    Decodes a list of bytes
    :param bytes_: 
    :return: decoded bytes
    :raises: ValueError
    """
    values, n = [], 0

    for idx, byt in enumerate(bytes_):
        n <<= 7
        n += (byt & SEVENBITSMASK)

        if byt & EIGHTBITMASK == 0:
            values.append(n)
            n = 0
        elif idx == len(bytes_) - 1:
            raise ValueError('incomplete byte sequence')

    return values
