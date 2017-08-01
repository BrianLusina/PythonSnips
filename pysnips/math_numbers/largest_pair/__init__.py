import heapq


class MaxProd(object):
    def __init__(self, array):
        self.array = array

    # slowest implementation
    def max_product_slow(self):
        n = sorted(self.array, reverse=True)
        return n[0] * n[1]

    # average of the three solutions
    def max_product_avg(self):
        count = 0
        m1 = m2 = float('-inf')
        for x in self.array:
            count += 1
            if x > m2:
                if x >= m1:
                    m1, m2 = x, m1
                else:
                    m2 = x
        return m1 * m2

    # faster solution
    def max_product_fast(self):
        first = max(self.array)
        second = max(n for n in self.array if n != first)
        return first * second

    # fastest solution
    def max_product_fastest(self):
        x = heapq.nlargest(2, self.array)
        return x[0] * x[1]


# fastest solution
def max_product(array):
    first = max(array)
    second = max(n for n in array if n != first)
    return second * first
