import binascii


class Converter():
    @staticmethod
    def to_ascii(h):
        return bytearray.fromhex(h).decode()

    @staticmethod
    def to_hex(s):
        return binascii.hexlify(s)


s = "Look mom, no hands"
h = "4c6f6f6b206d6f6d2c206e6f2068616e6473"

print "Testing for Converter class"
print(Converter.to_hex(s))  # ,h)
print(Converter.to_ascii(h))  # ,s)
print(Converter.to_hex(Converter.to_ascii(h)))  # ,h)
print(Converter.to_ascii(Converter.to_hex(s)))  # ,s)
