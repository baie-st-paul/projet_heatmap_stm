import datetime
import gtfs_kit as gk
import gtfs_kit.stop_times

from models import coordinate

feed = gk.read_feed("DataSource/gtfs_stm.zip", dist_units='km')
dataframe = gtfs_kit.stop_times.get_stop_times(feed)

donnees_Temps = [datetime.time(0, 0, 0)]
for i in range((24 * 4) - 1):
    donnees_Temps.append((datetime.datetime.combine(datetime.datetime.now(), donnees_Temps[i])
                         + datetime.timedelta(minutes=15)).time())


coordinate_start = coordinate.Coordinate(45.456619, -73.621198, 0)
coordinate_end = coordinate.Coordinate(45.422088, -73.578597, 0)





print()

print("Finished")