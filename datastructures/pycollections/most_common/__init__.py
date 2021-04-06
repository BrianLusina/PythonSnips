from collections import Counter, OrderedDict


class OrderCounter(Counter, OrderedDict):
    pass


[print(*c) for c in OrderCounter(sorted(input())).most_common(3)]
