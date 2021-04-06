class Complex(object):
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        s = Complex()
        s.real = self.real + other.real
        s.imag = self.imag + other.imag
        return s

    def __sub__(self, other):
        s = Complex()
        s.real = self.real - other.real
        s.imag = self.imag - other.imag
        return s

    def __mul__(self, other):
        s = Complex()
        s.real = self.real * other.real - self.imag * other.imag
        s.imag = self.real * other.imag + self.imag * other.real
        return s

    def __truediv__(self, other):
        s = Complex()
        s.real = (self.real * other.real + self.imag * other.imag) / (other.real ** 2 + other.imag ** 2)
        s.imag = (self.imag * other.real - self.real * other.imag) / (other.real ** 2 + other.imag ** 2)
        return s

    def mod(self):
        s = Complex()
        s.real = math.sqrt(self.real ** 2 + self.imag ** 2)
        return s

    def __str__(self):
        return '{0:.2f}{1:+.2f}i'.format(self.real, self.imag)
