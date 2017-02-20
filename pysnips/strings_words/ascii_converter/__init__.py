import binascii


def to_ascii(h):
    return bytearray.fromhex(bytes.decode(h)).decode()


def to_hex(s):
    return binascii.hexlify(str.encode(s))
