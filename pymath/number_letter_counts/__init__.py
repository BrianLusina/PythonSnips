from algorithms.say_number import say


def number_letter_counts(start, end):
    """
    counts all the letters used in the range of start to end, when each number is converted to words
    1 would become one, 2 would become two, etc,
    A range of 1 to 5 is one, two, three, four, five, number of letters used in total are 3 + 3 + 5 + 4 + 4 = 19

    An example:
    >>> number_letter_counts(1, 5)
    19

    :param start: Where to start the range
    :param end: Limit/end of the range
    :return: Returns the number of letters used in the range
    :rtype: int
    """
    # sanity checks

    # short circuit early if the start and end are the same
    if start == end or end == 0:
        return len(say(start))

    # if invalid values used, ie. None
    if end is None or start is None:
        raise ValueError(f"Start or end can not be None")

    if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
        raise ValueError(f"Expected number input")

    # enforce converting the input to integer
    start = int(start)
    end = int(end)

    # get the range
    num_range = range(start, end + 1)

    # map each number in range to say, converting it to words
    numbers_in_words = map(say, num_range)

    # iterate through each number, counting the number of letters used
    letters = 0

    # for each number in the range of words used
    for number in numbers_in_words:
        # count the number of letters used, excluding hyphens and spaces
        # find the letters used for this number
        letters_used = len(number) - (number.count(" ") + number.count("-"))

        letters += letters_used

    return letters
