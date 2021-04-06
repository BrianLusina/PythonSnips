def design_door_mat(n, m):
    """
    Designs a door mat given parameters n and m with constrains 5<n<101 and 15<m<303
    >>> design_door_mat(7, 21)
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    :param n: height of the mat
    :param m: length of the mat which is always 3 times the length
    :return: a designed door mat as a string with WELCOME at the center
    :rtype: str
    """
    # that each line has a set number of repetitions of '.|.', which are centered, and the rest is filled by '-'.
    # the flag is symmetrical, so if you have the top, you have the bottom by reversing it.
    # You only need to work on n // 2 (n is odd and you need the integer div because the remaining line is the "WELCOME" line).
    # generate 2*i + 1 '.|.', center it, and fill the rest with '-'.
    pattern = [(".|." * (2 * i + 1)).center(m, "-") for i in range(n // 2)]

    # join the pattern with the middle WELCOME line and the pattern reversed
    return "\n".join(pattern + ["WELCOME".center(m, "-")] + pattern[::-1])

# print(design_door_mat(7, 21))
