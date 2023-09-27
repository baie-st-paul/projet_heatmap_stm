import datetime
import gtfs_kit as gk
import gtfs_kit.stop_times
import pandas

from models import coordinate

feed = gk.read_feed("DataSource/gtfs_stm.zip", dist_units='km')
stop_time_dataframe = gtfs_kit.stop_times.get_stop_times(feed)
stop_dataframe = gtfs_kit.stops.get_stops(feed)
stop_dataframe["coordinate"] = stop_dataframe.apply(lambda row: coordinate.Coordinate(row[3], row[4], 0), axis=1)
join_stop = pandas.merge(stop_dataframe, stop_time_dataframe, on="stop_id")
start_coordinate = coordinate.Coordinate(45.450900, -73.621198, 0)
end_coordinate = coordinate.Coordinate(45.422088, -73.578597, 0)
print("shaving stop map...")
join_stop = join_stop[
    (join_stop["stop_lat"] < start_coordinate.latitude) &
    (join_stop["stop_lat"] > end_coordinate.latitude) &
    (join_stop["stop_lon"] > start_coordinate.longitude) &
    (join_stop["stop_lon"] < end_coordinate.longitude)
]

print("map is shaved well...")
def get_timedata_array():
    donnees_Temps = [datetime.time(0, 0, 0)]
    for i in range((24 * 4) - 1):
        donnees_Temps.append((datetime.datetime.combine(datetime.datetime.now(), donnees_Temps[i])
                              + datetime.timedelta(minutes=15)).time())

    return donnees_Temps


def get_coordinates_table(coordinate_start, coordinate_end):
    area_table = []
    area_table.append(coordinate_start)

    index_latitude = 0
    index_longitude = 0
    while area_table[index_longitude].longitude < coordinate_end.longitude:
        while area_table[index_latitude].latitude > coordinate_end.latitude:
            new_coordinate = coordinate.Coordinate(area_table[index_latitude].latitude - 0.000900,
                                                   area_table[index_latitude].longitude, 0)
            area_table.append(new_coordinate)
            index_latitude += 1

        new_coordinate = coordinate.Coordinate(area_table[index_longitude].latitude,
                                               area_table[index_longitude].longitude + 0.000900, 0)
        area_table.append(new_coordinate)
        index_longitude += 1

    return area_table


def get_area_table_at_time(area_table, start_time, join_stop):
    print()

    end_time = (datetime.datetime.combine(datetime.datetime.now(), start_time) + datetime.timedelta(minutes=15)).time()

    def convert_to_datetime(str):
        try:
            return bool(start_time <= datetime.datetime.strptime(str, "%H:%M:%S").time() < end_time)
        except (ValueError):
            return False


    join_stop["arrival_time"] = join_stop.apply(lambda row: convert_to_datetime(row["arrival_time"]), axis=1)

    join_stop = join_stop[join_stop["arrival_time"] == True]
    for area in area_table:
        print(area)
        join_stop["is_in_distance"] = join_stop.apply(lambda row: 1 if area.is_instde(row["coordinate"]) else 0, axis=1)
        area.intensity_factor = join_stop["is_in_distance"].sum()


    appended_area_table = []
    for area in area_table:
        if area.intensity_factor > 0:
            print(area)
            area.latitude = float(area.latitude)
            area.longitude = float(area.longitude)
            area.intensity_factor = int(area.intensity_factor)
            appended_area_table.append(area)

    return appended_area_table


print("Starting Process")




area_table = get_coordinates_table(
    start_coordinate,
    end_coordinate
)
timedata_array = get_timedata_array()

# serais fun d'etre un tableau pandas
area_table_per_time = []

index = 0


for time in timedata_array:
    print("process for :", time, "| index = ", index)
    area_table_per_time.append(get_area_table_at_time(area_table, time, join_stop))
    index += 1

#area_table_per_time.append(get_area_table_at_time(area_table, timedata_array[32], join_stop))
print("Process Finished")


def testtest(time_string):
    time = datetime.datetime.strptime(time_string, "%H:%M:%S").time()
    index = timedata_array.index(time)
    print("time at " ,timedata_array[index])

    return area_table_per_time[index]
