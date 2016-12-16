def prime_factors(number):
    c, res = 2, []
    while c * c <= number:
        while (number % c) == 0:
            # repeats multiple factors
            res.append(c)
            number /= c
        c += 1
    if number > 1:
        res.append(number)
    return res
