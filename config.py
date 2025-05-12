import os

def get_coordinates():
    lat = float(os.getenv("LATITUDE", "52.2297"))
    lon = float(os.getenv("LONGITUDE", "21.0122"))
    return lat, lon
