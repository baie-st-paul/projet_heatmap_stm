import math
from dataclasses import dataclass
from geopy import distance


@dataclass
class Coordinate:

    latitude:float
    longitude:float
    intensity_factor:int

    def distance(self, other):
        return distance.distance((self.latitude, self.longitude), (other.latitude, other.longitude)).m

