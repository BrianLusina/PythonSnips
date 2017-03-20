def design_door_mat(n, m):
    """
    Designs a door mat given parameters n and m with constrains 5<n<101 and 15<m<303
    :param n: height of the mat
    :param m: length of the mat which is always 3 times the length
    :return: a designed door mat as a string with WELCOME at the center
    :rtype: str
    """
    pattern = [(".|." * (2 * i + 1)).center(m, "-") for i in range(n // 2)]
    return "\n".join(pattern + ["WELCOME".center(m, "-")] + pattern[::-1])

