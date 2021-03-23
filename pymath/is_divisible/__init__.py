def is_divisible(*args):
    f = args[0]
    return all(f % x == 0 for x in args[1:])
