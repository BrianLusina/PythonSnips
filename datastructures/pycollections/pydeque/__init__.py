from collections import deque

N = int(input())
d = deque()
for _ in range(N):
    method, *args = input().split()
    getattr(d, method)(*args)
[print(x, end=" ") for x in d]
