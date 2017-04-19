class ShellGame(object):
    def __init__(self, start, swaps):
        self.start = start
        self.swaps = swaps

    def find_the_ball(self):
        if len(self.swaps) == 0:
            return self.start
        else:
            for pos in self.swaps:
                for x in pos:
                    self.start = x
        return self.start
