class SquareClimber(object):
    def __init__(self, number):
        self.number = number

    def climber(self):
        d = dict()
        for x in range(1, self.number + 1):
            d[x] = x ** 2
        return d


sq = SquareClimber(7)
print(sq.climber())
