import math

def long_conversion(lat, long):
    lat0 = 42.338574
    long0 = -71.0945489

    x = math.cos((lat + lat0) * 3.14 / 360)
    x = (long - long0) * 4000000 * x
    x = x / 360
    print(x)
