class Luhn(object):
    def __init__(self, number):
        self.number = number

    @staticmethod
    def addends():
        pass

    @staticmethod
    def checksum():
        pass

    def is_valid(self):
        return not sum(
            [d if i & 1 else d % 5 * 2 + d / 5 for i, d in enumerate(map(int, str(self.number).replace(" ", "")))]) % 10

    @staticmethod
    def create(number):
        pass
