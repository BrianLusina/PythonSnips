def tribonacci(n):
    print("Hold on, crunching numbers...\n"+"**"*10)
    c, res = 0, [0, 1, 1]
    if n == 0:
        return res
    while c <= n:
        next = res[c] + res[c + 1] + res[c + 2]
        res.append(next)
        c += 1
        if res[c] >= n:
            break
    print("Here is your tribonacci sequence!\n"+"--"*10)
    return res
