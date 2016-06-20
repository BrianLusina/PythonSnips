import random
#imports math module
import math
#imports specific functions from the module math
from math import sqrt,cos

for i in range(5):
	value = random.randint(1,6)
	print(value)

print(math.sqrt(25))

def func(x):
  res = 0
  for i in range(x):
     res += i
  return res

print(func(4))
