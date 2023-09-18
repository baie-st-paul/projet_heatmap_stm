import math
from geopy import distance

class Coordinate:
    def __init__(self, latitude, longitude, intensity_factor):
        self.latitude = latitude
        self.longitude = longitude
        self.intensity_factor = intensity_factor

    def distance(self, other):
        return distance.distance((self.latitude, self.longitude), (other.latitude, other.longitude)).m

    def __str__(self):
        return "Latitude: " + str(self.latitude) + ", Longitude: " + str(self.longitude) + ", Intensity Factor: " + str(self.intensity_factor)
