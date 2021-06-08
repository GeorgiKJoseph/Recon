import statistics as stat

DEFAULT_LAT = '10.011461'
DEFAULT_LON = '76.300799'

# Returns mean of coordinates
def getMapCenter(sights):
    latitudes  = [float(x.latitude) for x in sights]
    longitudes = [float(x.longitude) for x in sights]
    if len(latitudes) == 0:
        return DEFAULT_LAT, DEFAULT_LON
    center_lat = str(round(stat.mean(latitudes),6))
    center_lon = str(round(stat.mean(longitudes),6))
    return center_lat, center_lon