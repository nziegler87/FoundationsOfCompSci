import turtle

X_PERCENT = .75
Y_PERCENT = 1.0
Y_POS = 0

BLANK_PIECE = "./images/white.gif"

class Graphics:

    def __init__(self):
        '''
        Constructor -- creates an instance of graphics
        Attributes:
            screen -- screen turtle
            screen.tracer -- sets screen to update only when called
            screen.setup -- sets default screen parameters
            
            game_square -- creates a turtle to draw game squares
            game_square.hideturtle() -- hides turtle arrow
            game_square.up() -- so lines aren't drawn on screen while moving
            
            arrow -- creates a turtle to draw click arrows on screen
            arrow.hideturtle() -- hides turtle arrow
            arrow.up() -- so lines aren't drawn on screen while moving
        '''
        # set up screen turtle
        self.screen = turtle.Screen()
        self.screen.tracer(0)
        self.screen.setup(width = X_PERCENT, height = Y_PERCENT,
                          starty = Y_POS)

        # set up game_square turtle
        self.game_square = turtle.Turtle()
        self.game_square.hideturtle()
        self.game_square.up()

        # set up arrow turtle
        self.arrow = turtle.Turtle()
        self.arrow.hideturtle()
        self.arrow.up()
        
    def add_shape(self, image):
        self.screen.addshape(image)

    # DO I EVEN NEED TO SAVE X, Y...ARE THEY ABRITRARY ONCE DRAWN?
    def draw_piece(self, identifier, x, y, size, color, image = BLANK_PIECE):
        '''
        Method: draw_piece
        Paramters:
            self -- the current object
            identifier -- a string
            x -- center x coordinate of piece, an int (assumes square piece)
            y -- center y coordinate of piece, an int (assumes square piece)
            image -- file string for an image file (optional)
            size -- dimension of square piece, an int
            color -- turtle draw and fill color of piece, a string
        Does: draws one piece for overall game board
        '''
        self.game_square.color(color, color)

        # draw background square
        self.game_square.goto(x - (size / 2), y + (size / 2))
        self.game_square.down()
        self.game_square.begin_fill()
        for i in range(4):
            self.game_square.forward(size)
            self.game_square.right(90)
        self.game_square.end_fill()
        self.game_square.up()

        # stamp gamepiece image
        self.game_square.goto(x, y)
        self.game_square.shape(image)
        self.game_square.stamp()
        self.game_square.write(identifier, align = "center")
        self.screen.update()

    def draw_arrow(self, image, x, y):
        '''
        Method: draw_arrow
        Parameters:
            self -- the current object
            image -- the string for an image file
            x -- center x coordinate of piece, an int (assumes square piece)
            y -- center y coordinate of piece, an int (assumes square piece)
        '''
        self.arrow.goto(x, y)
        self.arrow.shape(image)
        self.arrow.stamp()
        self.screen.update()

    def update_piece(self, identifier, x, y, image):
        '''
        Method: update_piece
        Parameters:
            self -- the current object
            identifier -- a string
            x -- center x coordinate of piece, an int (assumes square piece)
            y -- center y coordinate of piece, an int (assumes square piece)
            image -- file string for an image file
        '''
        self.game_square.goto(x, y)
        self.game_square.shape(image)
        self.game_square.stamp()
        self.game_square.write(identifier, align = "center")
        self.screen.update()

    
