import turtle

# image constants
WHITE = "./images/white_piece_90.gif"
RED = "./images/red_piece_90.gif"
YELLOW = "./images/yellow_piece_90.gif"
ARROW = "./images/down_arrow2.gif"
SIZE = 100
COLOR = "blue"
IMG_LST = [WHITE, RED, YELLOW, ARROW]
GAME_PIECES = [WHITE, RED, YELLOW]

# window constants
X_PERCENT = .75
Y_PERCENT = 1.0
Y_POS = 0

def setup_screen():
    ''' Name: setup_screen
        Parameters: nothing
        Returns: name of variable where screen turtle object is saved
    '''
    screen = turtle.Screen()
    screen.tracer(0)
    
    screen.setup(width = X_PERCENT, height = Y_PERCENT,
                      starty = Y_POS)
    
    for image in IMG_LST:
        screen.addshape(image)

    return screen

def setup_piece():
    ''' Name: setup_piece
        Parameters: none
        Returns: variable where piece turtle object is saved
    '''
    piece = turtle.Turtle()
    piece.hideturtle()
    piece.up()

    return piece

def setup_arrow():
    ''' Name: setup_arrow
        Parameters: none
        Returns: variable where arrow turtle object is saved
    '''
    arrow =  turtle.Turtle()
    arrow.hideturtle()
    arrow.up()

    return arrow

def draw_piece(turtle, screen, identifier, x, y, image):
    ''' Name: draw_piece
        Parameters:
            turtle -- turtle object for drawing graphics
            screen -- turtle object for screen
            identifier -- a string
            x -- center x coordinate of piece, an int (assumes square piece)
            y -- center y coordinate of piece, an int (assumes square piece)
            image -- file string for an image file
        Returns: nothing
    '''
    turtle.color(COLOR, COLOR)
    turtle.shape(image)

    # draw background square
    turtle.goto(x - (SIZE / 2), y + (SIZE / 2))
    turtle.down()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(SIZE)
        turtle.right(90)
    turtle.end_fill()
    turtle.up()

    # stamp gamepiece image
    turtle.goto(x, y)
    turtle.shape(image)
    turtle.stamp()
    turtle.write(identifier, align = "center")
    screen.update()

def draw_arrow(turtle, screen, image, x, y):
    ''' Name: draw_arrow
        Parameters:
            turtle -- turtle object for drawing graphics
            screen -- turtle object for screen
            x -- center x coordinate of piece, an int (assumes square piece)
            y -- center y coordinate of piece, an int (assumes square piece)
            image -- file string for an image file
        Returns: nothing
    '''
    turtle.goto(x, y)
    turtle.shape(image)
    turtle.stamp()
    screen.update()
    
def draw_board(board, turtle, screen, image):
    ''' Name: draw_board
        Parameters:
            board -- nested list of game_piece objects where all rows have
                     same number of columns
            
        Returns: nothing
        Does: uses data found in game_piece objects (x cord, y cord, and image)
              to draw board on screen
    '''
    for i in range(len(board)):
        for j in range(len(board[0])):
            piece = board[i][j]
            draw_piece(turtle, screen, piece.identifier,
                       piece.x, piece.y, image)

def draw_arrows(arrow_lst, turtle, screen, image):
    ''' Name: draw_arrows
        Parameters:
            arrow_lst -- nested list of arrow objects
            turtle -- turtle object for drawing graphics
            screen -- turtle object for screen
            image -- file string for an image file
        Returns: nothing
    '''
    for arrow in arrow_lst:
        draw_arrow(turtle, screen, image, arrow.x, arrow.y)

def update_piece(turtle, screen, identifier, x, y, image):
    ''' Name: update_piece
        Parameters:
            turtle -- turtle object for drawing graphics
            screen -- turtle object for screen
            identifier -- a string
            x -- center x coordinate of piece, an int (assumes square piece)
            y -- center y coordinate of piece, an int (assumes square piece)
            image -- file string for an image file
        Returns:
            nothing
    '''
    turtle.goto(x, y)
    turtle.shape(image)
    turtle.stamp()
    turtle.write(identifier, align = "center")
    screen.update()
        
            
        
            
