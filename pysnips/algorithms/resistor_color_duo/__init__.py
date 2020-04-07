color_mapping = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
]


def value(colors):
    """
    Gets the Resistor color value of n resistors. Raises an exception if the length of the list is less than or equal to
    1.
    :param colors: List of resistor colors
    :type list
    :raises Exception
    :return: integer value of the resistor
    """
    if not colors:
        raise Exception("Expected colors to be an iterable")

    if len(colors) <= 1:
        raise Exception("Expected colors to be at least 2")
    
    return color_mapping.index(colors[0]) * 10 + color_mapping.index(colors[1])
