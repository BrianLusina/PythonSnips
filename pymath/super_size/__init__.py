def super_size(n):
    out = [i for i in str(n)]
    m = int("".join(list(sorted(out))[::-1]))
    return m


print(super_size(2150))
