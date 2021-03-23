from itertools import combinations


class Corners(object):
    def __init__(self, i, j):
        # i, j are position of corners
        self.i = i
        self.j = j

    def __str__(self):
        return "[" + str(self.i) + ", " + str(self.j) + "]"


def same_line(index, list_):
    """
    return corner on the same line
    :param index:
    :param list_:
    :return:
    """
    for c in list_:
        if c.i == index:
            return c


# return corner on the same column
def same_col(index, list_):
    for c in list_:
        if c.j == index:
            return c


def search_corners(rectangle):
    """
    Searches for cornes and returns the position of the corners as coordinates
    The cornes are represented with `+`
    :param rectangle: the input rectangle
    :return: a list of the coordinates of the corners
    :rtype: list
    """
    corner_list = []
    for i in range(0, len(rectangle)):
        for j in range(0, len(rectangle[i])):
            if rectangle[i][j] == "+":
                corner_list.append(Corners(i, j))
    return corner_list


def possible_rect(quartet):
    """
    validate that 4 points form a rectangle by comparing distance to centroid of the rectangle for all corners
    :param quartet: The four points of the rectangle
    :return: True if all 4 points have same distance to the centroid, False otherwise
    :rtype: bool
    """
    mid_x = 0
    mid_y = 0

    # centroid
    for c in quartet:
        mid_x += c.i / 4.0
        mid_y += c.j / 4.0

    # reference distance using first corner
    dx = abs(quartet[0].i - mid_x)
    dy = abs(quartet[0].j - mid_y)

    # Check all the same distance from centroid are equals
    for i in range(1, len(quartet)):
        if abs(quartet[i].i - mid_x) != dx or abs(quartet[i].j - mid_y) != dy:
            return False
    return True


def path(c1, c2, lines):
    """
    validate path between two corners
    :param c1: 1st corner
    :param c2: 2nd corner
    :param lines: The input lines
    :return: True if the path is valid
    :rtype: bool
    """
    if c1.i == c2.i:
        for j in range(min(c1.j + 1, c2.j + 1), max(c1.j, c2.j)):
            if lines[c1.i][j] != "-" and lines[c1.i][j] != "+":
                return False
        return True
    elif c1.j == c2.j:
        for i in range(min(c1.i + 1, c2.i + 1), max(c1.i, c2.i)):
            if lines[i][c1.j] != "|" and lines[i][c1.j] != "+":
                return False
        return True


def validate_rect(rect, lines):
    """
    validate path of rectangle by validating the connection at every corner
    with neighbours on the same line and col
    :param rect: The rectangle points
    :param lines: The input lines to validate if a rectangle
    :return: True if the lines are a valid rectangle
    :rtype: bool
    """
    for i in range(0, len(rect)):
        l = same_line(rect[i].i, rect[0:i] + rect[i + 1:])
        c = same_col(rect[i].j, rect[0:i] + rect[i + 1:])
        if not path(rect[i], l, lines) or not path(rect[i], c, lines):
            return False
    return True


def count(lines=""):
    """
    count number of rectangles inside ASCII in input lines
    :param lines:
    :return: Number of rectangles in the input linees
    """

    nb_rect = 0

    # test empty str
    if lines == "":
        return nb_rect

    # search for the corners of the rectangle
    corners = search_corners(lines)

    # no corners in str
    if len(corners) == 0:
        return nb_rect

    # now let the magic begin
    # all combinations of 4 corners (python ftw)
    q = list(combinations(corners, r=4))
    rectangles = []

    # check if all 4 corners are valid rectangles
    for el in q:
        if possible_rect(el):
            rectangles.append(el)

    # validate path in found rectangles
    for rect in rectangles:
        if validate_rect(rect, lines):
            nb_rect += 1
    return nb_rect
