def multiiter(*args):
    if len(args) == 1:
        yield args
    else:
        for x, y in args:
            for a in range(x):
                for b in range(y):
                    yield (a, b)
