from game_board import *
import turtle
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
TEXT_COLOR = "black"
SCORE_COLOR = "blue"
HEADING_COLOR = "green"

# window constants
W_X_PERCENT = .8
W_Y_PERCENT = .8
Y_POS = 0

# message constants
X_PERCENT = .7
Y_PERCENT = .2
CURRENT_PLAYER_X_OFFSET = 100
CURRENT_IMG_Y_OFFSET = 50
SCORE_Y_OFFSET = 150
POP_BORDER = "black"
POP_FILL = "light grey"
ANIMATION_DELAY = .05
POPUP_DELAY = 2

def setup_screen():
    ''' Name: setup_screen
        Parameters: nothing
        Returns: name of variable where screen turtle instance is saved
    '''
    screen = turtle.Screen()
    screen.tracer(0)

    screen.setup(width = W_X_PERCENT, height = W_Y_PERCENT,
                      starty = Y_POS)

    # add all game shapes to screen
    for image in IMG_LST:
        screen.addshape(image)

    return screen

def setup_turtle():
    ''' Name: setup_turtle
        Parameters: none
        Returns: variable where piece turtle istance is saved
    '''
    draw = turtle.Turtle()
    draw.hideturtle()
    draw.up()

    return draw

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

    # go back to center and stamp piece image
    turtle.goto(x, y)
    turtle.stamp()

def draw_board(board, turtle, screen, image):
    ''' Name: draw_board
        Parameters:
            board -- nested list of game_piece objects where all rows have
                     same number of columns
            turtle -- turtle object for drawing graphics
            screen -- turtle object for screen
            image -- file string for an image file
        Returns: nothing
        Does: uses data found in game_piece objects (x cord, y cord, and image)
              to draw board on screen
    '''
    for i in range(len(board)):
        for j in range(len(board[0])):
            piece = board[i][j]
            draw_piece(turtle, screen, piece.x, piece.y, image)

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

def draw_arrows(arrow_lst, turtle, screen, image):
    ''' Name: draw_arrows
        Parameters:
            arrow_lst -- list of arrow objects
            turtle -- turtle object for drawing graphics
            screen -- turtle object for screen
            image -- file string for an image file
        Returns: nothing
    '''
    for arrow in arrow_lst:
        draw_arrow(turtle, screen, image, arrow.x, arrow.y)

    screen.update()
        
def update_current_player(turtle, screen, x, y, current_player, current_image):
    ''' Name: update_current_player_text
        Parameters: turtle and screen instances
                    x_cord and y_cords of top left corner of board (floats)
                    current_player name (a string), and game piece image (str)
        Returns: nothing
    '''
    turtle.clear()

    # write text
    x -= CURRENT_PLAYER_X_OFFSET
    turtle.goto(x, y)
    turtle.color(HEADING_COLOR)
    turtle.write("Current Player", align = C_ALIGN, font = (FONT, SIZE, STYLE))

    turtle.goto(x, y - SIZE)
    turtle.color(TEXT_COLOR)
    turtle.write(current_player, align = C_ALIGN, font = (FONT, SIZE, STYLE))

    # stamp image
    y -= CURRENT_IMG_Y_OFFSET
    turtle.goto(x, y)
    turtle.shape(current_image)
    turtle.stamp()
    
    screen.update()

def display_scores(turtle, screen, player_lst, x, y):
    ''' Name: display_scores
        Parameters: turtle and screen instances
                    list with two player instances
                    x and y coordinates for to left corner of board (floats)
        Returns: nothing
    '''
    turtle.clear()
    x -= CURRENT_PLAYER_X_OFFSET
    y -= SCORE_Y_OFFSET
    
    turtle.goto(x, y)
    turtle.color(HEADING_COLOR)
    turtle.write("Total Games Won", align = C_ALIGN, font = (FONT, SIZE, STYLE))

    # write header and value in different colors
    for player in player_lst:
        name = player.name
        score = str(player.score)

        y -= SIZE
        turtle.goto(x, y)
        turtle.color(TEXT_COLOR)
        turtle.write(name, align = C_ALIGN, font = (FONT, SIZE, STYLE))

        y -= SIZE
        turtle.goto(x, y)
        turtle.color(SCORE_COLOR)
        turtle.write(score, align = C_ALIGN, font = (FONT, SIZE, STYLE))

        turtle.color(TEXT_COLOR)
        y -= SIZE
        turtle.goto(x, y)

    screen.update()

def update_piece(turtle, screen, start_y, x, y, image, size):
    ''' Name: update_piece
        Parameters:
            turtle -- turtle object for drawing graphics
            screen -- turtle object for screen
            x -- center x coordinate of piece, an int (assumes square piece)
            y -- center y coordinate of piece, an int (assumes square piece)
            image -- file string for an image file
            size -- size of game piece (an int)
        Returns: nothing
        Does: updates a blank game piece to appropriate color, temporarily
              updating any blank game pieces between top row of game pieces
              and target piece, simulating animation
    '''
    while start_y > y:
        turtle.goto(x, start_y)
        turtle.shape(image)
        turtle.stamp()
        screen.update()
        
        turtle.shape(WHITE_IMG)
        time.sleep(ANIMATION_DELAY)
        turtle.stamp()
        screen.update()
        start_y -= size
        
    turtle.goto(x, start_y)
    turtle.shape(image)
    turtle.stamp()
    screen.update()
   
def popup_box(turtle, screen, starting_x, starting_y,
                 num_rows, num_cols, piece_size, text):
    ''' Name: popup_box
        Parameters:
            turtle -- turtle object for drawing
            screen -- turtle object for screen
            starting_x -- x coordinate of top left game piece
            starting_y -- y coordinate of top left game piece
            num_rows -- number of rows, an int
            num_cols -- number of cols, an int
            piece_size -- size of game pieces, an int
            text -- text, a string, to be printed
        Returns: nothing
        Does: creates a popup box on screen and prints message
    '''
    # use board and game piece details to calculate size of popup box
    board_x = abs(num_cols * piece_size)
    board_y = abs(num_rows * piece_size)
    center_x = starting_x - (piece_size / 2) + board_x / 2
    center_y = starting_y + (piece_size / 2) - board_y / 2
    box_width = board_x * X_PERCENT
    box_height = board_y * Y_PERCENT

    # draw message box
    turtle.goto(center_x - (box_width / 2), center_y + (box_height / 2))
    turtle.color(POP_BORDER, POP_FILL)
    turtle.begin_fill()
    turtle.down()
    for i in range(2):
        turtle.forward(box_width)
        turtle.right(90)
        turtle.forward(box_height)
        turtle.right(90)
    turtle.end_fill()
    turtle.up()

    # write text in window
    turtle.goto(center_x, center_y)
    turtle.write(text, align = C_ALIGN, font = (FONT, SIZE, STYLE))
    
    screen.update()

    time.sleep(POPUP_DELAY)
    turtle.clear()
            
