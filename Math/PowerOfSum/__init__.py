def power_sum_dig_term(n):
    return power_of_sum()[n-1]


def power_of_sum():
    lst_n = []
    for base in range(2, 100):
        num = base
        for _ in range(2, 30):
            num *= base
            if sum(map(int, str(num))) == base:
                lst_n.append(num)
    return sorted(lst_n)
