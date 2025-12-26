from algorithms.backtracking.word_search.point import Point

# points on cartesian plan enclosing the word grid
PLANE_LIMITS = (
    Point(1, 0),
    Point(1, -1),
    Point(1, 1),
    Point(-1, -1),
    Point(0, -1),
    Point(0, 1),
    Point(-1, 1),
    Point(-1, 0),
)
