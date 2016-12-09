class Product(object):
    def __init___(self, l):
        self.l = l

    def product(self):
        result = 1
        for i in self.l:
            result = result * i
        return result
