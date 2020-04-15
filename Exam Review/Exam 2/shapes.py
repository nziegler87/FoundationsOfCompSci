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
class Octogon(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
