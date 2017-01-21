import binascii


class HexToDex(object):
    def __init__(self, hex_string):
        self.hex_string = hex_string

    def hex_to_dec(self):
        return int(self.hex_string, 16)

    # alternative version using binascii
    def hex_to_dec_binascii(self):
        return int.from_bytes(binascii.unhexlify(("0" * (len(self.hex_string) % 2)) + self.hex_string), byteorder="big")
