import datetime
import gtfs_kit as gk
import gtfs_kit.stop_times
from models import coordinate
from flask import Flask, request, jsonify

app = Flask(__name__)

feed = gk.read_feed("DataSource/gtfs_stm.zip", dist_units='km')
stop_time_dataframe = gtfs_kit.stop_times.get_stop_times(feed)
stop_dataframe = gtfs_kit.stops.get_stops(feed)


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


area_table = get_coordinates_table(
    coordinate.Coordinate(45.450900, -73.621198, 0),
    coordinate.Coordinate(45.422088, -73.578597, 0)
)

print("Starting")


def get_area_table_at_time(area_table, start_time):
    end_time = (datetime.datetime.combine(datetime.datetime.now(), start_time) + datetime.timedelta(minutes=15)).time()

    stop_times_between = []
    for stop_time in stop_time_dataframe.values:
        if datetime.datetime.strptime(stop_time[1], "%H:%M:%S").time() >= end_time:
            break
        if datetime.datetime.strptime(stop_time[1], "%H:%M:%S").time() >= start_time:
            stop_times_between.append(stop_time)

    stops = []
    for time in stop_times_between:
        stops.append(stop_dataframe.loc[stop_dataframe["stop_id"] == time[3]].values[0])

    index = 0
    for area in area_table:
        for stop in stops:
            if area.distance(coordinate.Coordinate(stop[3], stop[4], 0)) < 51:
                area_table[index].intensity_factor = area_table[index].intensity_factor + 1
        index += 1

    return area_table


test = get_area_table_at_time(area_table, datetime.time(8, 0, 0))

print("Finished")


@app.get("/areaAtTime")
def get_test():
    return test
