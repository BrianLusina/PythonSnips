"""
Implement a function that successfully adds two numbers together and returns their solution in binary. The conversion can be done before, or after the addition of the two.

The binary number returned should be a string!
"""
def add_binary(a,b):
    return '{0:b}'.format(a+b)

print(add_binary(1,1),"10")
print(add_binary(0,1),"1")
print(add_binary(1,0),"1")
print(add_binary(2,2),"100")
print(add_binary(51,12),"111111")
