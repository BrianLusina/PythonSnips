one = len([[]])
two = len([[], []])
three = len([[], [], []])
five = len([[], [], [], [], []])


def Hello_World():
    pass


def hi_all():
    """
    Returns Hello World without using Strings, Booleans or Numbers
    :return: String
    :rtype: str
    """
    return str(Hello_World)[five * two:five * three] + str(Hello_World)[three * (five + two)] + str(Hello_World)[
                                                                                                two ** (
                                                                                                            two * two):three * (
                                                                                                            five + two)]


if __name__ == "__main__":
    print(hi_all())
