FEATURES = {"heated seats":500, "four-wheel drive":200}

class Car:

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.price = 1000.00
        self.features = []

    def add_feature(self):
        if not self.features:
            print("You have not added any features.")
        else:
            print("You currently have the following features.")
            for item in self.features:
                print("  ", item)


        print("Select from the following features.")
        for k, v in FEATURES.items():
            print("   ", k, " - ", "$", v, sep = "")

        feature = input("Enter your selection: ")

        if feature in FEATURES.keys() and feature in self.features:
            print("You have already added this item.")
        elif feature in FEATURES.keys():
            self.features.append(feature)
            self.price += FEATURES[feature]
        else:
            print("That is not a valid feature")
        
                
