from itertools import cycle


def replicate_iter(times, data):
    if not isinstance(times, int):
        raise ValueError
    for item in cycle(data):
        for _ in range(times):
            yield(item)


def replicate_recur(times, data):
    if times == 0 or times == 1:
        return [data]
    else:
        m = replicate_recur(times-1, data)
        m.append(data)
        return m


result = replicate_iter(3, 5)
print([result], [5, 5, 5])
