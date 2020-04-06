import turtle
from game_board import *
import time

# image constants
WHITE_IMG = "./images/white_piece_60.gif"
RED_IMG = "./images/red_piece_60.gif"
YELLOW_IMG = "./images/yellow_piece_60.gif"
ARROW_IMG = "./images/down_arrow2_40.gif"
COLOR = "blue"
IMG_LST = [WHITE_IMG, RED_IMG, YELLOW_IMG, ARROW_IMG]

# default font constants
C_ALIGN = "center"
FONT = "arial"
SIZE = 15
STYLE = "bold"

# window constants
W_X_PERCENT = .8
W_Y_PERCENT = .8
Y_POS = 0

# message constants
X_PERCENT = .7
Y_PERCENT = .2
CURRENT_PLAYER_X_OFFSET = 100
CURRENT_IMG_Y_OFFSET = 50

def setup_screen():
    ''' Name: setup_screen
        Parameters: nothing
        Returns: name of variable where screen turtle object is saved
    '''
    screen = turtle.Screen()
    screen.tracer(0)
    
    screen.setup(width = W_X_PERCENT, height = W_Y_PERCENT,
                      starty = Y_POS)
    
    for image in IMG_LST:
        screen.addshape(image)

    return screen

def setup_turtle():
    ''' Name: setup_turtle
        Parameters: none
        Returns: variable where piece turtle object is saved
    '''
    draw = turtle.Turtle()
    draw.hideturtle()
    draw.up()

    return draw

def display_text(box, screen, starting_x, starting_y, num_rows, num_cols, size, text):
    x_size = abs(num_cols * size)
    y_size = abs(num_rows * size)
    center_x = starting_x - (size / 2) + x_size / 2
    center_y = starting_y + (size / 2) - y_size / 2
    box_width = x_size * X_PERCENT
    box_height = y_size * Y_PERCENT
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
    box.write(text, align = C_ALIGN, font = (FONT, SIZE, STYLE))
    screen.update()

def update_current_player(turtle, screen, x, y, current_player, current_image):
    ''' Name: update_current_player_text
        Parameters: x_cord and y_cords of top left corner of board (floats)
                    current_player name ( a string)
        Returns: nothing
    '''
    turtle.clear()

    # write text
    x -= CURRENT_PLAYER_X_OFFSET
    turtle.goto(x, y)
    turtle.write("Current Player:", align = C_ALIGN, font = (FONT, SIZE, STYLE))
    turtle.goto(x, y - SIZE)
    turtle.write(current_player, align = C_ALIGN, font = (FONT, SIZE, STYLE))

    # stamp image
    y -= CURRENT_IMG_Y_OFFSET
    turtle.goto(x, y)
    turtle.shape(current_image)
    turtle.stamp()
 
def draw_piece(turtle, screen, x, y, image):
    ''' Name: draw_piece
        Parameters:
            turtle -- turtle object for drawing graphics
            screen -- turtle object for screen
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

    # go back to center and stamp piece
    turtle.goto(x, y)
    turtle.stamp()

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
            draw_piece(turtle, screen, piece.x, piece.y, image)

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

def update_piece(turtle, screen, start_y, x, y, image, size):
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
    print(start_y)
    print(y)
    while start_y > y:
        turtle.goto(x, start_y)
        turtle.shape(image)
        turtle.stamp()
        screen.update()
        turtle.shape(WHITE_IMG)
        time.sleep(.05)
        turtle.stamp()
        screen.update()
        start_y -= size
    turtle.goto(x, start_y)
    turtle.shape(image)
    turtle.stamp()
    screen.update()
    
        
            
        
            
