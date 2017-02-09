def replicate_iter(times, data):
    """
    Will replicate the data a number of times, if the data is a valid object, float, int, str
    and the times to repeat is an integer, else a ValueError is raised.
    Will use iteration instead to repeat the data a number of times.
    :param times: number of times to repeat the data
    :param data: data to repeat
    :return: a list with the data having been repeated a  number of times
    :rtype: list
    :raises: ValueError
    """
    if (isinstance(data, (float, int, str))) and isinstance(times, int):
        return [data for _ in range(0, times) if times > 0]
    else:
        raise ValueError("Invalid data or times input")


def replicate_recur(times, data):
    """
    Will recursively repeat data a number of times.
    :param times: the number of times to repeate the data
    :param data: item to be repeated
    :return: data to be repeated a number of times.
    :rtype: list
    """
    if isinstance(data, (float, int, str)) and isinstance(times, int):
        if times > 0:
            ls = replicate_recur(times - 1, data)
            ls.append(data)
            return ls
        else:
            return []
    else:
        raise ValueError
