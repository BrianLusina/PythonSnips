def nb_dig(n, d):
    squares = [x ** 2 for x in range(0, n + 1)]
    return sum([str(i).count(str(d)) for i in squares if str(d) in str(i)])
