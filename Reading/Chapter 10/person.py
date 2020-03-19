class Person:
    def __init__(self, weight = 100):
        self.__name = "unnamed"
        self.__weight = weight
        self.__age = 33

    def get_age(self):
        return self.__age

    def get_weight(self):
        return self.__weight

    def get_name(self):
        return self.__name

class Person2:
    def __init__(self, weight = 100):
        self.name = "unnamed"
        self.weight = weight
        self.age = 33
