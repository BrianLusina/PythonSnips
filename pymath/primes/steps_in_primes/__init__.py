from ..is_prime import is_prime


def step(g, m, n):
    if (n - m) < g:
        return None

    if (n - m) == g and (is_prime(m) and is_prime(n)):
        return [m, n]

    for x in range(m, n + 1):
        second = x + g

        if is_prime(x) and is_prime(second):
            return [x, second]

    return None
