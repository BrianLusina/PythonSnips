def replicate_iter(times, data):
    if (isinstance(data, (float, int, str))) and isinstance(times, int):
        ls = []
        if times > 0:
            for i in range(1, times + 1):
                ls.append(data)
        return ls
    else:
        raise ValueError


def replicate_recur(times, data):
    if isinstance(data, (float, int, str)) and isinstance(times, int):
        if times > 0:
            ls = replicate_recur(times - 1, data)
            ls.append(data)
            return ls
        else:
            return []
    else:
        raise ValueError
