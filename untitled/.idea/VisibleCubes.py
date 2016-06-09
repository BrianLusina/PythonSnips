"""
Description:

Imagine there's a big cube consisting of n^3 small cubes. Calculate, how many small cubes are not visible from outside.

For example, if we have a cube which has 4 cubes in a row, then the function should return 8, because there are 8 cubes inside our cube (2 cubes in each dimension)
"""
class VisibleCubes:
    def __init__(self,n):
        self.n = n

    @classmethod
    def cubearea(cls, n):
        return cls (n)

    #method to calculate the area
    def calc_area(self):
        return str(pow(n, 3)) + " cm3"

    #check on the visible cubes
    @staticmethod
    def visible_cubes(n):
        return pow(n, 3) - VisibleCubes.not_visible_cubes(n)

    #check on how many cubes are not visible
    @staticmethod
    def not_visible_cubes(n):
        return 0 if n in range(0, 3) else (n-2)**3
      
def test(n,m):
    return n == m

print test(VisibleCubes.not_visible_cubes(0), 0)
print test(VisibleCubes.not_visible_cubes(1), 0)
print test(VisibleCubes.not_visible_cubes(2), 0)
print test(VisibleCubes.not_visible_cubes(3), 1)
print test(VisibleCubes.not_visible_cubes(4), 8)