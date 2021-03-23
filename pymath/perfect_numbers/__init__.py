def is_perfect(number):
    return sum(divisor_generator(number)) + 1 == number


def divisor_generator(n):
    """ Returns an unordered list of divisors for n (1 < n). """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            yield i
            if i * i != n:
                yield n // i

