def mod7(n):
    for x in range(n+1):
        if x % 7 == 0:
            yield x


print(list(mod7(50)))
