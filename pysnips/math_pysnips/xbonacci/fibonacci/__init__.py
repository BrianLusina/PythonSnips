def fib(a, b, end):
    c = 0
    fib_list = [a, b]
    if end == 0:
        return fib_list
    while c < end:
        nxt = fib_list[c] + fib_list[c+1]
        fib_list.append(nxt)
        c += 1
        if nxt >= end:
            break
    return fib_list


def fib_memo(n):
    known = {0: 0, 1: 1}
    if n in known:
        return known[n]

    res = fib_memo(n - 1) + fib_memo(n - 2)
    known[n] = res
    return res

