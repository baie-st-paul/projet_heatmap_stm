import math
from dataclasses import dataclass
from geopy import distance


@dataclass
class Coordinate:
    latitude: float
    longitude: float
    intensity_factor: int

    def distance(self, other):
        return distance.distance((self.latitude, self.longitude), (other.latitude, other.longitude)).m

    def is_instde(self, other):
        if (self.latitude + 0.000450 > other.latitude > self.latitude - 0.000450 and
                self.longitude + 0.000450 > other.longitude > self.longitude - 0.000450):
            return True
        else:
            return False
