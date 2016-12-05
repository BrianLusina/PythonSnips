from math import sqrt

def is_triangle_number(number):
    if not isinstance(number, int):
        return False
    x = (sqrt(8*number + 1) - 1) / 2
    if x - int(x) > 0:
    	return False
    return True
#return n * (n+1) / 2