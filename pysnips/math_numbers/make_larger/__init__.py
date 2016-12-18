class MakeLarger(object):
    def __init__(self, number):
        self.number = number

    # shorter time to complete
    def make_larger_v0(self):
        l = []
        for x in str(self.number):
            l.append(x)
        s = sorted(l, reverse=True)
        return int("".join(s))

    def make_larger_v1(self):
        str_number = str(self.number)
        sorted_lst = sorted([x for x in str_number], reverse=True)
        return int("".join(sorted_lst))

    # takes a longer time to complete the problem
    def make_larger_v2(self):
        return int("".join(sorted([x for x in str(self.number)], reverse=True)))
