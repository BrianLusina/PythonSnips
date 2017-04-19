def square_of_sum(n):
    return sum(range(n+1))**2


def sum_of_squares(n):
    return sum([x**2 for x in range(n+1)])


def difference(d):
    return square_of_sum(d) - sum_of_squares(d)