def accum(s):
    c, res = 0, []
    for x in [x for x in s]:
        res.append(x * (c + 1))
        c += 1
    return "-".join([x[0].upper() + x[1:].lower() for x in res])
