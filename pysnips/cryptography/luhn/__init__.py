class Luhn(object):
    def __init__(self, number):
        self.number = number

    def addends(self):
        def transform(val):
            return (2 * val - 9) if (val > 4) else (2 * val)
        dig = [int(d) for d in str(self.number)]
        return [(transform(x) if (i % 2 == 0) else x)
                for i, x in enumerate(dig, start=len(dig) % 2)]

    def checksum(self):
        return sum(self.addends())

    def is_valid(self):
        return self.checksum() % 10 == 0

    @staticmethod
    def create(num):
        p = (10 - Luhn(num * 10).checksum()) % 10
        return 10 * num + p
