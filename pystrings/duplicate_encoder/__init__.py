class DuplicateEncoder(object):
    def __init__(self, encode):
        self.encode = encode

    def duplicate_encode(self):
        encode = self.encode.lower()
        out = ""
        for x in encode:
            if encode.count(x) == 1:
                out += "("
            else:
                out += ")"
        return out

    def duplicate_encode_v2(self):
        return "".join(["(" if self.encode.lower().count(c) == 1 else ")" for c in self.encode.lower()])
