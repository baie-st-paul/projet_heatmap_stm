import datetime
import gtfs_kit as gk
import gtfs_kit.stop_times

from models import coordinate
"""
feed = gk.read_feed("DataSource/gtfs_stm.zip", dist_units='km')
dataframe = gtfs_kit.stop_times.get_stop_times(feed)

donnees_Temps = [datetime.time(0, 0, 0)]
for i in range((24 * 4) - 1):
    donnees_Temps.append((datetime.datetime.combine(datetime.datetime.now(), donnees_Temps[i])
                         + datetime.timedelta(minutes=15)).time())

"""

def get_coordinates_table(coordinate_start, coordinate_end):
    area_table = []
    area_table.append(coordinate_start)


    index_latitude = 0
    index_longitude = 0
    while area_table[index_longitude].longitude < coordinate_end.longitude:
        while area_table[index_latitude].latitude > coordinate_end.latitude:
            new_coordinate = coordinate.Coordinate(area_table[index_latitude].latitude - 0.000900, area_table[index_latitude].longitude, 0)
            area_table.append(new_coordinate)
            index_latitude += 1

        new_coordinate = coordinate.Coordinate(area_table[index_longitude].latitude, area_table[index_longitude].longitude + 0.000900, 0)
        area_table.append(new_coordinate)
        index_longitude += 1

    return area_table

area_table = get_coordinates_table(
    coordinate.Coordinate(45.450900, -73.621198, 0),
    coordinate.Coordinate(45.422088, -73.578597, 0)
)

print(len(area_table))
print("Finished")