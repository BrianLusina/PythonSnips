# using heapq module
# A priority queue that holds cube sums. When consecutive sums come out with the same value, they are taxis.
from heapq import heappush, heappop


def cubesum():
    h, n =[], 1
    while True:
        while not h or h[0][0] > n**3:
            heappush(h, (n**3 + 1, n, 1))
            n += 1

        (s, x, y) = heappop(h)
        yield((s, x, y))
        y += 1
        if y < x:
            heappush(h, (x**3, y**3, x, y))


def taxis():
    out =[(0, 0, 0)]
    for x in cubesum():
        if x[0] == out[-1][0]:
            out.append(x)
        else:
            if len(out) > 1:
                yield out
                out = [x]


n = 0
for x in taxis():
    n += 1
    if n >= 2006:
        break
    if n <= 25 or n >= 2000:
        print(n, x)
