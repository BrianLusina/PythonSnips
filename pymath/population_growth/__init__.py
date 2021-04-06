def nb_year(p0, percent, aug, p):
    n = 0
    while p0 < p:
        p0 += p0 * (percent / 100) + aug
        n += 1
    return n
