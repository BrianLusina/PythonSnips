class Divisible5(object):
    def __init__(self, binary_lst):
        self.binary_lst = binary_lst

    def div_five(self):
        return ",".join([x for x in self.binary_lst.split(",") if int(x, 2) % 5 == 0])

    def div_five_tw0(self):
        lst = []
        for x in self.binary_lst.split(","):
            if int(x, 2) % 5 == 0:
                lst.append(x)
        return ",".join(lst)
