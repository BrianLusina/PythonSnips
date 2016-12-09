class EvenDigits(object):
    def __init__(self, number_range):
        self.number_range = number_range

    def evens(self):
        return ",".join([str(x) for x in self.number_range if
                         int(str(x)[0]) % 2 == 0 and int(str(x)[1]) % 2 == 0 and int(str(x)[2]) % 2 == 0])


evn = EvenDigits(range(1000, 3001))
print(evn.evens())
