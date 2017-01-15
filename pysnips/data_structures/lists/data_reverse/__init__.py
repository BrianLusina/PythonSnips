def data_reverse(data):
    """
    Picks the stream of data and converts it into bits, then reverses the input
    :param data:
    :return:
    """
    # byte store
    byte_store = []
    reversed_bytes = []

    # length of 8/16/32/64/ multiple of 8
    data_len = len(data)

    count = 0
    while count < data_len:
        byte_store.append(data[count: count + 8])
        count += 8

    for byte in reversed(byte_store):
        reversed_bytes += byte
    return reversed_bytes


# an alternative solution
def data_reverse_(data):
    """
    Reverses a stream of bytes
    :param data:
    :return:
    """
    return [b for a in range(len(data) - 8, -1, -8) for b in data[a:a + 8]]
