def climb(n):
    return [1] if n == 1 else climb(int(n / 2)) + [n]


print(list(climb(13)))
