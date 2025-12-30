class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed

    def set_closed(self, closed: bool) -> None:
        # set the flag for closed/open
        self.closed = closed

    def __str__(self):
        return (
            "[" + str(self.start) + ", " + str(self.end) + "]"
            if self.closed
            else "(" + str(self.start) + ", " + str(self.end) + ")"
        )

    def __eq__(self, other: "Interval") -> bool:
        return self.start == other.start and self.end == other.end
