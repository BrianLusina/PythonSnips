import cProfile
from functools import reduce


def power_sum_dig_term(n):
    return power_of_sum()[n - 1]


def power_of_sum():
    lst_n = []
    for base in range(2, 100):
        num = base
        for _ in range(2, 30):
            num *= base
            if sum(map(int, str(num))) == base:
                lst_n.append(num)
    return sorted(lst_n)


# Alternatively
series = [0]
for a in range(2, 99):
    for b in range(2, 42):
        c = a ** b
        if a == sum(map(int, str(c))):
            series.append(c)
power_sumDigTerm = sorted(series).__getitem__

# alternative 2
sum_dig = lambda n: reduce(lambda x, y: x + int(y), str(n), 0)

memo = []

for i in range(2, 100):
    for j in range(1, 100):
        p = i ** j
        if p > 10 and sum_dig(p) == i: memo += [p]

memo.sort()


def power_sumDigTerm_2(n):
    return memo[n - 1]


def main():
    cProfile.run('power_of_sum()')


if __name__ == "__main__":
    main()
