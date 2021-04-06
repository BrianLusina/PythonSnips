import math


def robot_mover(*s):
    pos = [0, 0]
    for x in s:
        direction = x[0]
        if direction == "UP":
            pos[0] += x[1]
        elif direction == "DOWN":
            pos[0] -= x[1]
        elif direction == "LEFT":
            pos[1] -= x[1]
        elif direction == "RIGHT":
            pos[1] += x[1]
    return {"Position": pos, "Distance from origin": int(round(math.sqrt(pos[1] ** 2 + pos[0] ** 2)))}


print(robot_mover(("UP", 5), ("DOWN", 3), ("LEFT", 3), ("RIGHT", 2)))
