import gtfs_kit as gk

feed = gk.read_feed("DataSource/gtfs_stm.zip", dist_units='km')
print(feed)

print("Finished")