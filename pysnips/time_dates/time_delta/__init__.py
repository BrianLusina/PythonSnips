from datetime import datetime as dt

fmt = "%a %d %b %Y %H:%M:%S %z"
for _ in range(int(input())):
    diff = dt.strptime(input(), fmt) - dt.strptime(input(), fmt)
    print(int(abs(diff.total_seconds())))