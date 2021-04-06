def song(start, stop=0):
    """
    :param start: in which verse to start singing
    :param stop: where to stop
    :return: the snippet of the song
    """
    result = ""
    for number in reversed(range(stop, start + 1)):
        result += verse(number) + "\n"

    return result


def verse(verse_no):
    """
    :param verse_no: The verse number to start from
    :return: the verse
    """
    return "".join([
        "%s of beer on the wall, " % _bottles(verse_no).capitalize(),
        "%s of beer.\n" % _bottles(verse_no),
        _action(verse_no),
        _next_bottle(verse_no)
    ])


def _bottles(number):
    if number == 0:
        return "no more bottles"
    if number == 1:
        return "1 bottle"
    else:
        return "%d bottles" % number


def _action(number):
    if number == 0:
        return "Go to the store and buy some more, "
    else:
        return "Take {} down and pass it around, ".format("one" if number > 1 else "it")


def _next_bottle(number):
    return "%s of beer on the wall.\n" % _bottles(_next_verse(number))


def _next_verse(number):
    return number - 1 if number > 0 else 99
