def sum_same(num, times):
    c, total = 1, 0
    while c <= times:
        n = str(num) * c
        total += int(n)
        c += 1
    return total
