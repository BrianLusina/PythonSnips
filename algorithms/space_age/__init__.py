def converter(period):
    def inner(self):
        return round(self.seconds / period, 2)

    return inner


class SpaceAge(object):
    __earth_orbital = 31557600
    SPACE_YEARS = {"earth": __earth_orbital, "mercury": 0.2408467 * __earth_orbital,
                   "venus": 0.61519726 * __earth_orbital, "mars": 1.8808158 * __earth_orbital,
                   "jupiter": 11.862615 * __earth_orbital, "saturn": 29.447498 * __earth_orbital,
                   "uranus": 84.016846 * __earth_orbital, "neptune": 164.79132 * __earth_orbital}

    def __init__(self, seconds):
        self.seconds = seconds

    on_earth = converter(SPACE_YEARS["earth"])
    on_mercury = converter(SPACE_YEARS["mercury"])
    on_venus = converter(SPACE_YEARS["venus"])
    on_mars = converter(SPACE_YEARS["mars"])
    on_jupiter = converter(SPACE_YEARS["jupiter"])
    on_uranus = converter(SPACE_YEARS["uranus"])
    on_saturn = converter(SPACE_YEARS["saturn"])
    on_neptune = converter(SPACE_YEARS["neptune"])
