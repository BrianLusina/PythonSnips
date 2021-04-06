def dominator(arr):
    res = 0
    if len(arr) == 0:
        return -1
    for x in arr:
        if arr.count(x) > len(arr) / 2:
            res = x
            break
        else:
            res = -1
    return res
