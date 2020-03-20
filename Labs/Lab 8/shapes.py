'''
    Class: Shape.
    This is the Abstract superclass that defines our shape protocol
'''    
class Shape:
    def __init__(self):
        self.name = 'Generic Shape'
    def draw(self):
        print('I don\'t know how to draw')
    def area(self):
        return 0
    def introduce_yourself(self):
        print('I\'m too shy!')

'''
    Class: Square.
    This is a Concrete class that is a subclass of Shape
    It knows how to draw itself, calculate its area, compare to other
    Squares (for equality) and introduce itself to its audience
'''    
class Square(Shape):
    def __init__(self, length):
        super().__init__() 
        self.length = length
        self.name = 'Square'
    def draw(self):
        print('+---+\n|   |\n+---+\n')
    def area(self):
        return round(self.length**2,2)
    def __str__(self):
        return self.name
    def __eq__(self, other):
        if self.length == other.length:
            return True
        return False
    def introduce_yourself(self):
        print('Hello! I\'m a ', self.name, '. Nice to meet you!')
        print('I like dogs, cats and food. Here is my sign: ')
        self.draw()
        print('My area is ', self.area())

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        self.name = "Circle"
    def draw(self):
        print("   +  +   \n +      + \n   +  +   \n")
    def area(self):
        import math
        return round(math.pi * (self.radius ** 2), 2)
    def __str__(self):
        return self.name
    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        return False
    def introduce_yourself(self):
        print("Hello! I'm a ", self.name, ". Nice to meet you!", sep = "")
        print("I don't like dogs or cats but love food. Here is my sign:")
        self.draw()
        print("My area is ", self.area())

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.name = "Triangle"
        self.base = base
        self.height = height
    def draw(self):
        print("    ^    \n   / \  \n  /   \ \n  _____ \n")
    def area(self):
        return round((.5 * (self.base * self.height)), 0)
    def __str__(self):
        return self.name
    def __eq__(self, other):
        if self.area == other.area:
            return True
        return False
    def introduce_yourself(self):
        print("Hello! I'm a ", self.name, ". Nice to meet you!", sep = "")
        print("My head comes to a point, so people don't like me. Here is my "
              "sign:")
        self.draw()
        print("My area is ", self.area())

def shape_factory():
    import random
    classes = ["Square", "Circle", "Triangle"]
    selection = random.choice(classes)
    if selection == "Square":
        shape = Square(random.randint(1, 100))
    elif selection == "Circle":
        shape = Circle(random.randint(1, 100))
    else:
        shape = Triangle(random.randint(1, 100), random.randint(1, 100))
    return shape

def get_snarky_msg():
    import random
    messages = ["In every single way that was just everything I hated.",
                "It was a little bit like… uh… annoying girl singing in the bedroom.",
                "Thank you. No.", "You’ve just invented a new form of torture.",
                "You look like a pen salesman.",
                "You couldn’t win this competition if you were the only one in it… in a million years.",
                "Can I stop this? Because I’m bored out of my mind.",
                "Even your dog is struggling to get out of the room after that.",
                "No, we’re not going to give you any love. It was a terrible audition.",
                "It’s just rubbish.", "You have the personality of a mouse.",
                "America would hate you."]
    print("Simon says: ", random.choice(messages), sep = "")
    
def main():
    for i in range(10):
        shape = shape_factory()
        shape.introduce_yourself()
        print()
        get_snarky_msg()
        print("\n")

main()
