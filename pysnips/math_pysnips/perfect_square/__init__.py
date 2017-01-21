from math import sqrt


# function to check if a number is a perfect square
def is_square(n):
    if n < 0:
        return False
    else:
        return sqrt(n).is_integer()
