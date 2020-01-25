def lat_conversion(lat):
    ''' Inputs: Latitude coordinate (float) to be converted to
                y coordinate as float
        Returns: y coordinate
        Does: Calculates y coordinates from user inputed latitude
    '''

    lat0 = 42.338574

    y = ((lat - lat0) * 4000000) / 360

    return y
