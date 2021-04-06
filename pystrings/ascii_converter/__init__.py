import binascii


def to_ascii(h):
    encoded = str.encode(h)
    return bytearray.fromhex(bytes.decode(encoded)).decode()


def to_hex(s):
    return str(binascii.hexlify(str.encode(s)))
