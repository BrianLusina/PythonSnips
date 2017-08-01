class VisibleCubes:
    def __init__(self, n):
        self.n = n

    @classmethod
    def cubearea(cls, n):
        return cls(n)

    # method to calculate the area
    def calc_area(self):
        return str(pow(self.n, 3)) + " cm3"

    # check on the visible cubes
    @staticmethod
    def visible_cubes(n):
        return pow(n, 3) - VisibleCubes.not_visible_cubes(n)

    # check on how many cubes are not visible
    @staticmethod
    def not_visible_cubes(n):
        return 0 if n in range(0, 3) else (n - 2) ** 3
