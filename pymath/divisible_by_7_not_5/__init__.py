class Divisible7(object):
    """
    class that gets all the numbers divisible by 7, but not by 5 in a range
    """

    def __init__(self, rnge):
        self.rnge = rnge

    def div7(self):
        return ",".join([str(x) for x in self.rnge if x % 7 == 0 and x % 5 != 0])

    # solution two
    def div7_two(self):
        l = []
        for i in self.rnge:
            if (i % 7 == 0) and (i % 5 != 0):
                l.append(str(i))
        return ','.join(l)


lst = Divisible7(range(2000, 3201))
print(lst.div7())
