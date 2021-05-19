def tribonacci(sig, n):
    res = sig
    c = 0
    if n == 0:
        return []
    elif n in range(1, 4):
        return sig[0:n]
    while c <= n:
        next = res[c] + res[c + 1] + res[c + 2]
        res.append(next)
        c += 1
        if len(res) == n:
            break
    return res


def nth_tribonacci(n: int) -> int:
    sig = [0, 1, 1]

    if n in sig:
        return n

    first = sig[0]
    second = sig[1]
    third = sig[2]

    for _ in range(3, n + 1):
        fourth = first + second + third
        first = second
        second = third
        third = fourth

    return third
