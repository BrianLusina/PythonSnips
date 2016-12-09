def song(start, stop=0):
    pass


def verse(verse_no):
    """
    :param verse_no: The verse number to start from
    :return: the verse
    """
    return "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some" \
           " more, 99 bottles of beer on the wall.\n " if verse_no == 0 \
        else "{} bottle{} of beer on the wall, {} bottle{} of beer.\nTake {} down and pass it around, {}" \
        .format(verse_no, "s" if verse_no > 1 else "", verse_no, "s" if verse_no > 1 else "",
                "it" if verse_no == 1 else "one",
                "no more bottles of beer on the wall.\n" if verse_no - 1 == 0
                else str(verse_no - 1) + " bottles of beer on the wall.\n")
