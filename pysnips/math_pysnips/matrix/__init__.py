class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = [[int(n) for n in row.split()] for row in matrix.split('\n')]
        self.columns = [list(tup) for tup in zip(*self.rows)]

    def alternative(self):
        rows = [map(int, item.split()) for item in self.matrix.split("\n")]
        columns = [map(list, zip(*rows))]

    def alternative_2(self):
        rows = [[int(x) for x in line.split()] for line in self.matrix.split("\n")]
        columns = [[rows[r][c]
                    for r in range(len(rows))]
                   for c in range(len(rows[0]))]
