def tribonacci(n):
    c, res = 0, [0, 1, 1]
    if n == 0:
        return res
    while c <= n:
        next = res[c] + res[c + 1] + res[c + 2]
        res.append(next)
        c += 1
        if len(res) == n:
            break
    return res
