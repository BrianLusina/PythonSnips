def slices(number, n):
    initial, res = 0, []
    if n > len(number) or n == 0:
        raise ValueError("Desired slices greater than number length")
    elif n == len(number):
        return [[int(x) for x in number]]
    elif n == 1:
        return [[int(x)] for x in number]
    else:
        while n <= len(number):
            res.append([int(x) for x in number[initial:n]])
            initial += 1
            n += 1
    return res