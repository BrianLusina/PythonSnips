class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = [[int(n) for n in row.split()] for row in matrix.split('\n')]
        self.columns = [list(tup) for tup in zip(*self.rows)]
