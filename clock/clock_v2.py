class Clock():
    """
    Variation of clock. This is the second way of doing it
    """
    def __init__(self, hour, minute):
        self.total = (hour * 60 + minute) % (24 * 60)

    # define the hour property and get the floor division, this returns the exact hour
    @property
    def hour(self):
        return self.total // 60

    # returns the minutes exactly
    @property
    def minute(self):
        return self.total % 60

    # converts to a string
    def __str__(self):
        return "%02d:%02d" % (self.hour, self.minute)

    # checks for equality
    def __eq__(self, other):
        return self.total == other.total

    # adds minutes to the clock
    def add(self, minutes):
        return Clock(self.hour, self.minute + minutes)

