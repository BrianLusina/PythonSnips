def productFib(prod):
    fib, res, indx = [0, 1], [], 0
    for _ in fib:
        if fib[indx] * fib[indx + 1] == prod:
            res = [fib[indx], fib[indx + 1], True]
            break
        if fib[indx] * fib[indx + 1] > prod:
            res = [fib[indx], fib[indx + 1], False]
            break
        fib.append(fib[indx] + fib[indx + 1])
        indx += 1
    return res


def productFib_v2(prod):
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]
