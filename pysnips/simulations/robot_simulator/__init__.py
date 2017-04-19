# initialize the compass points
NORTH, EAST, SOUTH, WEST = range(4)


class CompassPoints(object):
    """
    initialize the class to have a default compass bearing of NORTH
    left method subtracts a 'co-ordinate' point from the x axis
    right method moves the robot +1 co-ordinate along the x-axis
    """
    compass_points = [NORTH, EAST, SOUTH, WEST]

    def __init__(self, c_bearing=NORTH):
        self.c_bearing = c_bearing

    def move_left(self):
        self.c_bearing = self.compass_points[self.c_bearing - 1]

    def move_right(self):
        self.c_bearing = self.compass_points[(self.c_bearing + 1) % 4]


class Robot(object):
    """
    Initialize the ROBOT to have a bearing of north and x,y coordinates at the origin
    :compass_points is an instance(object) of the CompassPoints class
    :robot_bearing finds the current bearing of the robot
    :coordinates gets the current co-ordinates of the robot
    :advance method moves the robot across the plane based on the robot bearing, adding and subtracting coordinates
    :left_turn, right_turn moves the robot according to the input commands
    """

    def __init__(self, robot_bearing=NORTH, x_cord=0, y_cord=0):
        self.compass_points = CompassPoints(robot_bearing)
        self.x_cord = x_cord
        self.y_cord = y_cord

    @property
    def bearing(self):
        return self.compass_points.c_bearing

    @property
    def coordinates(self):
        return self.x_cord, self.y_cord

    def advance(self):
        if self.bearing == NORTH:
            self.y_cord += 1
        elif self.bearing == SOUTH:
            self.y_cord -= 1
        elif self.bearing == EAST:
            self.x_cord += 1
        elif self.bearing == WEST:
            self.x_cord -= 1

    def turn_left(self):
        return self.compass_points.move_left()

    def turn_right(self):
        return self.compass_points.move_right()

    def simulate(self, robot_commands):
        instruct = {'A': self.advance, 'R': self.turn_right, "L": self.turn_left}

        for cmd in robot_commands:
            if cmd in instruct:
                instruct.get(cmd)()
