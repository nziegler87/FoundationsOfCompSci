class Planet:
    ''' class Planet
        WHAT ELSE?
    '''
    def __init__(self, name, radius, mass, distance, num_moons):
        self.__name = name
        self.__radius = radius
        self.__mass = mass
        self.__distance = distance
        self.__num_moons = num_moons

    def get_name(self):
        return self.__name

    def get_radius(self):
        return self.__radius

    def get_mass(self):
        return self.__mass

    def get_distance(self):
        return self.__distance

    def get_moons(self):
        return self.__num_moons

    def get_volume(self):
        import math
        v = 4/3 * math.pi * self.__radius**3
        return round(v, 2)

    def get_surface_area(self):
        import math
        sa = 4 * math.pi * self.__radius**2
        return sa

    def get_density(self):
        d = self.mass / self.get_volume()
        return d

    def set_name(self, new_name):
        self.__name = new_name

    def set_moons(self, new_moons):
        self.__num_moons = new_moons

    
