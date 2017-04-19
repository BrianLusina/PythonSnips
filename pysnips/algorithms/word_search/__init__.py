from copy import copy


class Point(object):
    """
    Defines the blueprint of a specific point on the word grid. This point will be used to mark the position of
    a word on the cartesian plane.
    """

    def __init__(self, x, y):
        """
        Creates a new cartesian point object
        :param x: point on x-axis
        :param y: point on y-axis
        """
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({}:{})'.format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not (self == other)


# points on cartesian plan enclosing the word grid
PLANE_LIMITS = (
    Point(1, 0), Point(1, -1), Point(1, 1), Point(-1, -1),
    Point(0, -1), Point(0, 1), Point(-1, 1), Point(-1, 0)
)


class WordSearch(object):
    def __init__(self, puzzle):
        """
        Creates a new word search object
        :ivar self.width will be the length of the width for this word-search object, which is the length of the
        first item in the list.
        It is assumed that all items will have same length
        :ivar self.height will be the height of thw object, in this case, just the length of the list
        :param puzzle: the puzzle which will be a tuple of words separated by newline characters
        """
        self.rows = puzzle.split()
        self.width = len(self.rows[0])
        self.height = len(self.rows)

    def search(self, word):
        """
        Searches for a word in the puzzle
        :param word: word to search for in puzzle
        :return: the points where the word can be found, None if the word does not exist in the puzzle
        :rtype: Point
        """
        # creates a generator object of points for each letter in the puzzle
        positions = (Point(x, y) for x in range(self.width) for y in range(self.height))
        for pos in positions:
            for plane_limit in PLANE_LIMITS:
                result = self.find_word(word=word, position=pos, plane_limit=plane_limit)
                if result:
                    return result
        return None

    def find_word(self, word, position, plane_limit):
        """
        Finds the word on the puzzle given the word itself, the position (Point(x, y)) and the plane limit
        :param word: the word we are currently searching for, e.g python
        :param position: the current point on cartesian plan for the puzzle e.g Point(0, 0)
        :param plane_limit: the current plan limit, e.g Point(1, 0)
        :return: The Point where the whole word can be found
        :rtype: Point
        """
        # create a copy of the passed in position
        curr_position = copy(position)
        for let in word:
            if self.find_char(coord_point=curr_position) != let:
                return
            curr_position += plane_limit
        return position, curr_position - plane_limit

    def find_char(self, coord_point):
        """
        finds a character on the given puzzle
        :param coord_point: The current copy of the current point position being sought through
        :return:
        """
        if coord_point.x < 0 or coord_point.x >= self.width:
            return
        if coord_point.y < 0 or coord_point.y >= self.height:
            return
        # return the particular letter in the puzzled
        return self.rows[coord_point.y][coord_point.x]
