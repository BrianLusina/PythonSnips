

class BowlingGame(object):
    def __init__(self):
        pass

    def roll(self, pins):
        pass

    def score(self):
        pass


class Frame(object):
    """
    Divides up the array of rolls into Frame Objects
    """
    def __init__(self):
        self.rolls = [None, None]
        self.open = True

    def roll(self, roll, bonus_roll, accrued_bonuses, seen_bonus):
        # if it is a strike, we close the frame
        if roll = 10:
            self.rolls[0] = 10
            self.rolls[1] = 0
            self.open = False
        else:
            # first roll but frame is still open
            if self.rolls[0] == None:
                self.rolls[0] = roll

                # may need to close bonus rolls before we see 2 have been seen
                if bonus_roll and seen_bonus == accrued_bonuses:
                    self.rolls[1] = 0
                    self.open = False
            else:
                # second roll closes frame
                self.rolls[1] = roll
                self.open = False
    
    def is_open(self):
        return self.open

    def get_frame(self):
        return self.rolls


