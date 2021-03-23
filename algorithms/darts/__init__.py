from math import sqrt


def score(x, y):
    """
    Gets the score of a dart on a dart board
    :param x X coordinate of the dart
    :type int
    :param y Y coordinate of the dart
    :type int
    :return: Score based on location of dart
    :rtype int
    """

    dart_location = sqrt(x*x + y*y)

    if dart_location <= 1.0:
        return 10
    elif dart_location <= 5.0:
        return 5
    elif dart_location <= 10.0:
        return 1
    else:
        return 0
