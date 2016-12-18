def multiiter(*args):
    print(args)
    for x, y in args:
        for a in range(x):
            for b in range(y):
                yield (a, b)
