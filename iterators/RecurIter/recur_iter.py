def replicate_iter(times, data):
    pass


def replicate_recur(times, data):
    if times == 0 or times == 1:
        return [data]
    else:
        m = replicate_recur(times-1, data)
        m.append(data)
        return m

