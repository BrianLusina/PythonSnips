import binascii


def to_ascii(h):
    return bytearray.fromhex(h).decode()


def to_hex(s):
    return binascii.hexlify(s)
