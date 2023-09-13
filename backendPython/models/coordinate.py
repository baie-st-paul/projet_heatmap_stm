import math


class Coordinate:
    def __init__(self, latitude, longitude, intensity_factor):
        self.latitude = latitude
        self.longitude = longitude
        self.intensity_factor = intensity_factor

    def distance(self, other):
        return math.sqrt((self.latitude - other.latitude) ** 2 + (self.longitude - other.longitude) ** 2)

