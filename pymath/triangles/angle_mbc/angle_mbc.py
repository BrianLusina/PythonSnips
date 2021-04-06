import math

ab = int(input())
bc = int(input())

# using SOHCAHTOA
angle = round(math.degrees(math.atan2(ab, bc)))
print(str(angle) + "°")
