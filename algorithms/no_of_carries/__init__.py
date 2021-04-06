from itertools import zip_longest


def number_of_carries(a, b):
    carries = 0

    a = [int(n) for n in str(a)]
    b = [int(n) for n in str(b)]

    additions = abs(len(a) - len(b))

    if additions > 0:
        if len(a) > len(b):
            b = [0] * additions + b
        else:
            a = [0] * additions + a

    a = reversed(a)
    b = reversed(b)

    pairs = zip(a, b)

    current_sum = 0
    carrying = 0

    for x, y in pairs:
        current_sum = x + y + carrying

        if current_sum >= 10:
            carrying = 1
            carries += 1
        else:
            carrying = 0

    return carries


def number_of_carries_2(a, b):
    ans, carrie = 0, 0
    while a > 0 or b > 0:
        carrie = (a % 10 + b % 10 + carrie) // 10
        ans += [0, 1][carrie > 0]
        a //= 10
        b //= 10
    return ans


def number_of_carries_3(a, b):
    a, b = str(a)[::-1], str(b)[::-1]
    result = c = 0
    for x, y, in zip_longest(map(int, a), map(int, b), fillvalue=0):
        c = (x, y, c) > 9
        result += c
    return result
