import turtle

class Graphics:

    def __init__(self):
        self.screen = turtle.Screen()
        self.game_square = turtle.Turtle()
        self.game_square.hideturtle()
        self.screen.tracer(0)
        self.game_square.up()


    def add_shape(self, image):
        self.screen.addshape(image)

    def draw_piece(self, x, y, image, size, color):
        self.game_square.color(color, color)
        
        self.game_square.goto(x - (size / 2), y + (size / 2))
        self.game_square.down()
        self.game_square.begin_fill()
        for i in range(4):
            self.game_square.forward(size)
            self.game_square.right(90)
        self.game_square.end_fill()
        self.game_square.up()
        
        self.game_square.goto(x, y)
        self.game_square.shape(image)
        self.game_square.stamp()
        self.screen.update()

    def update_piece(self, x, y, image):
        self.game_square.goto(x, y)
        self.game_square.shape(image)
        self.game_square.stamp()
        self.screen.update()        
