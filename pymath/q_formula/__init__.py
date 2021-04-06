import math


class QFormula(object):
    """
    calculates the square root of the value from the formula [(2 * C * D)/H]
    """

    def __init__(self, number_list):
        self.number_list = number_list
        self.constant_c = 50
        self.constant_h = 30

    # using list compression
    def q_formula_compress(self):
        return ",".join([str(math.sqrt((float(x) * self.constant_c * 2) / self.constant_h)) for x in self.number_list])

    # using simple for loop
    def q_formula_simple(self):
        values = []
        for y in self.number_list:
            n = math.sqrt((float(y) * self.constant_c * 2) / self.constant_h)
            values.append(n)
        return ",".join(values)
