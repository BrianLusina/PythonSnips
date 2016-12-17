class TwoDimensions(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dimensions(self):
        row, col = self.x, self.y
        mult = [[0 for _ in range(col)] for _ in range(row)]
        for r in range(row):
            for c in range(col):
                mult[r][c] = r * c
        return mult
