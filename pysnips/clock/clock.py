class Clock(object):
    """
    Initialize the clock, such that
    __eq__ performs a comparison between the format intended and the input
    __repr__ How to represent the format
    clean() cleans up the clock,
    """
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.clean()

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __repr__(self):
        return "%02d:%02d" % (self.hour, self.minute)

    def add(self, minutes):
        self.minute += minutes
        return self.clean()

    def clean(self):
        self.hour += self.minute // 60
        self.hour %= 24
        self.minute %= 60
        self.hour += self.minute
        return self

