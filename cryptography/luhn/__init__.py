class Luhn(object):
    def __init__(self, number):
        if isinstance(number, int):
            self.number = number
        else:
            card_list = list((map(int, number.replace(" ", ""))))
            self.number = "".join(str(digit) for digit in card_list)

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
    def is_card_valid(card):
        """
        The input is a string with the full credit card number,
        in groups of 4 digits separated by spaces, i.e. "1234 5678 9012 3456"
        checks if a card number is valid
        :param card, card number as a string
        :return:
        """
        return Luhn(card).is_valid()

    @staticmethod
    def create(num):
        p = (10 - Luhn(num * 10).checksum()) % 10
        return 10 * num + p
