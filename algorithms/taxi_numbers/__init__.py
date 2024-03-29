# using heapq module
# A priority queue that holds cube sums. When consecutive sums come out with the same value, they are taxis.
from heapq import heappop, heappush


def cubesum():
    h, n = [], 1
    while True:
        while not h or h[0][0] > n**3:
            heappush(h, (n**3 + 1, n, 1))
            n += 1

        (s, a, b) = heappop(h)
        yield ((s, a, b))
        b += 1
        if b < a:
            heappush(h, (a**3, b**3, a, b))


def taxis():
    out = [(0, 0, 0)]
    for s in cubesum():
        if s[0] == out[-1][0]:
            out.append(s)
        else:
            if len(out) > 1:
                yield out
                out = [s]


n = 0
for x in taxis():
    n += 1
    if n >= 2006:
        break
    if n <= 25 or n >= 2000:
        print(n, x)
