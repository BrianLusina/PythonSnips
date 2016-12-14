from collections import defaultdict
from itertools import product
from pprint import pprint

cube2n = {x**3:x, for x in range(1, 1201)}
sum2cubs = defaultdict(set)

for c1, c2 in product(cube2n, cube2n):
    if c1 >= c2: sum2cubes[c1 + c2].add((cube2n[c1], cube2n[c2]))

