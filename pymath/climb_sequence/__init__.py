def climb(n):
    c, new_l, n_range = 0, [], list(range(1, n + 1))
    # if n is odd
    if n == 1 or n == 0:
        return new_l.append(n)
    if n % 2 != 0:
        i = (n - 1) / 2
        new_l.append(i)
        # i is now even
        if i % 2 == 0:
            i = i / 2
            new_l.append(i)
        new_l = list(reversed(new_l))
    # else if n is even
    else:
        i = n / 2
        new_l.append(i)
        # i is now odd
        if i % 2 != 0:
            i = (i - 1) / 2
            new_l.append(i)

        new_l = list(reversed(new_l))
