import turtle
from game_board import *

# image constants
WHITE_IMG = "./images/white_piece_60.gif"
RED_IMG = "./images/red_piece_60.gif"
YELLOW_IMG = "./images/yellow_piece_60.gif"
ARROW_IMG = "./images/down_arrow2_40.gif"
COLOR = "blue"
IMG_LST = [WHITE_IMG, RED_IMG, YELLOW_IMG, ARROW_IMG]

# window constants
X_PERCENT = .5
Y_PERCENT = .5
Y_POS = 0

CURRENT_PLAYER_X_OFFSET = 100
CURRENT_IMG_X_OFFSET = 125
CURRENT_IMG_Y_OFFSET = 50

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

def setup_current_player_text(x, y):
    ''' Name: setup_text
        Parameters: x_cord and y_cords where text to be printed (floats)
        Returns: variable where text turtle object is saved
    '''
    text = turtle.Turtle()
    text.hideturtle()
    text.up()
    x -= CURRENT_PLAYER_X_OFFSET
    text.goto(x, y)

    return text

def setup_box_message():
    box = turtle.Turtle()
    box.hideturtle()
    box.up()

    return box

def display_text(box, screen, starting_x, starting_y, num_rows, num_cols, size, text):
    x_size = abs(num_cols * size)
    y_size = abs(num_rows * size)
    center_x = starting_x - (size / 2) + x_size / 2
    center_y = starting_y + (size / 2) - y_size / 2
    box_width = x_size * .70
    box_height = y_size * .20
    box.goto(center_x - (box_width / 2), center_y + (box_height / 2))
    box.color("black", "light blue")
    box.begin_fill()
    box.down()
    for i in range(2):
        box.forward(box_width)
        box.right(90)
        box.forward(box_height)
        box.right(90)
    box.end_fill()
    box.up()
    box.goto(center_x, center_y)
    box.write(text, align = "center", font = ("arial", 15, "bold"))
    screen.update()


def update_current_player_text(turtle, current_player):
    ''' Name: update_current_player_text
        Parameters: name of current player (string)
        Returns: nothing
    '''
    turtle.clear()
    turtle.write("Current Player\n" + str(current_player),
                 align = "center", font = ("Arial", 14, "bold"))

def update_current_player_img(turtle, current_player_img, x, y):
    ''' Name: update_current_player_img
        Parameters: a turtle instance and image string
        Returns: nothing
    '''
    x -= CURRENT_IMG_X_OFFSET
    y -= CURRENT_IMG_Y_OFFSET
    turtle.goto(x, y)
    turtle.shape(current_player_img)
    turtle.stamp()
    
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
    turtle.goto(x - (PIECE_SIZE / 2), y + (PIECE_SIZE / 2))
    turtle.down()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(PIECE_SIZE)
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
        
            
        
            
