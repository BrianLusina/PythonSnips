def tribonacci(sig, n):
    res = sig
    c = 0
    if n == 0: return []
    elif n in range(1, 4):
        return sig[0:n]
    while c <= n:
        next = res[c]+ res[c+1] + res[c+2]
        res.append(next)
        c += 1
        if len(res) == n:
            break
    return res

