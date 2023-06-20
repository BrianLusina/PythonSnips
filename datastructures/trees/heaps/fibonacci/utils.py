import math


def floor_log(x):
    return math.frexp(x)[1] - 1
