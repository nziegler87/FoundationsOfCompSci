'''
    CS 5001
    Nathanial Ziegler
    February 5, 2020
    HW 3
    Description:
        UPDATE
'''

ROW_PER_PAGE = 3
COL_PER_PAGE = 4
PIXEL_PER_LINE = 4
PIXEL_SIZE = 10
IMAGE_OPTIONS = ["BIG", "LITTLE"]

# Constants for draw_pixel function
SIDES_IN_SQUARE = 4
RIGHT_TURN = 90

from render_images import *
from compress_functions import *
import turtle

def validate_input(user_input, option_list):
    ''' Name: validate_input
        Inputs: user_input, list of options
        Returns: True if user_input is in list of options
        Does: Compares user_input to options and returns True
              if user_input matches one of the responses.
    '''
    if user_input in option_list:
        return True

def ask_image_size():
    ''' Name: ask_image_size
        Input: nothing
        Returns: nothing
    '''
    print("Do you want to render a big or small image?")

def input_to_file(user_selection):
    ''' Name: input_to_file
        Input: user selection as a string
        Return: filename variable based on user input
        Does: returns BIG_IMG if user enters "BIG" or LITTLE_IMG if
              user enters "LITTLE"
    '''
    if user_selection == "BIG":
        return BIG_IMG
    else:
        return LITTLE_IMG

def decompress(compressed_list):
    ''' Name: decompress
        Input: nested list of strings where pixel streaks have been combined
        Returns: nested list where pixels treaks have been separated
        Does: decompresses nested pixel list
    '''
    decompressed_list = []

    # Iterate through each item in nested list of strings
    for i in range(len(compressed_list)):
        page_list = []
        for j in range(len(compressed_list[i])):

            # Use split string function to separate number and pixel color
            item = compressed_list[i][j].split(" ")
            number = int(item[0])
            pixel = item[1]

            # Add pixel(s) based on number denoted in streak and add to list
            for num in range(number):
                page_list.append(pixel)

        # Add decompressed pixels to master list
        decompressed_list.append(page_list)

    return(decompressed_list)

def collect_image_size(option_list):
    ''' Name: collect_image_size
        Input: list of user options, each as string
        Returns: name of file to be generated
    '''
    # Ask if user wants to render the BIG or LITLE image
    selection = input("Enter BIG or LITTLE: ").upper()

    # Call validate input to ensure response is valid
    while not validate_input(selection, option_list):
        selection = input("You must enter either BIG or LITTLE. " + \
                          "Try again: ").upper()

    # Call input_to_file to return variable name
    file = input_to_file(selection)

    return file

def set_start_cord(draw_turtle, original_list, PIXEL_SIZE):
    '''
        Does: sets turtle to render pixels at starting cord,
              based on pixel list and size
    '''
    draw_turtle.up()
    y_cord = determine_y_start(original_list, PIXEL_SIZE)
    x_cord = determine_x_start(original_list, PIXEL_SIZE)
    draw_turtle.goto(-(x_cord),(y_cord))

def draw_pixel(turtle, color, pixel_size):
    ''' Name: draw_pixel
        Input: turtle name, color of turtle (str), pixel_size (int)
        Returns: nothing
        Does: Draws one "pixel" based on pixel size and color
    '''
    turtle.hideturtle()
    turtle.down()
    turtle.color(color, color)
    turtle.begin_fill()
    for i in range(SIDES_IN_SQUARE):
        turtle.forward(pixel_size)
        turtle.right(RIGHT_TURN)
    turtle.end_fill()
    turtle.up()

def pixel_to_color(pixel):
    ''' Name: pixel_to_color
        Input: string (single pixel color represented by a letter)
        Returns: string (single pixel color as word)
        Does: Converts single letter pixel colors to colors readable by turtle
    '''
    if pixel == "P":
        color = "purple"
    elif pixel == "B":
        color = "black"
    elif pixel == "L":
        color = "light blue"
    elif pixel == "Y":
        color = "yellow"
    elif pixel == "O":
        color = "brown"
    else:
        color = "red"

    return color

def draw_page(turtle, pixel_list):
    ''' Input: turtle name, list of pixels (strs)
        Returns: nothing
        Does: Draws one page of pixels
    '''
    # Iterate through each row, rendering pixels
    j = 0
    for i in range(1, PIXEL_PER_LINE):
        start_x = turtle.xcor()
        start_y = turtle.ycor()
        
        # Render pixel for each row using pixel_to_color and draw_pixel functions
        while j < ((i * PIXELS_PER_LINE)):
            color = pixel_to_color(pixel_list[j])
            draw_pixel(turtle, color, PIXEL_SIZE)
            turtle.forward(10)
            j += 1

        # Move turtle to starting point but down a row of pixles
        turtle.goto(start_x, (start_y - PIXEL_SIZE))
               

def draw_image(turtle, image_list):
    image_col = calculate_col_pages(image_list, COL_PER_PAGE)
    print("Image col: ", image_col)
    image_row = calculate_row_pages(image_list, ROW_PER_PAGE)
    print("Image row: ", image_row)
    for i in range(0,3):
        start_x = turtle.xcor()
        start_y = turtle.ycor()
        pixel_list = image_list[i]
        draw_page(turtle, pixel_list)
        turtle.goto((start_x + (PIXEL_SIZE * COL_PER_PAGE)), start_y)
    turtle.goto((start_x - COL_PER_PAGE * PIXEL_SIZE * 2), # Why this?
                (start_y - ROW_PER_PAGE * PIXEL_SIZE))
    for i in range(3,6):
        start_x = turtle.xcor()
        start_y = turtle.ycor()
        pixel_list = image_list[i]
        draw_page(turtle, pixel_list)
        turtle.goto((start_x + (PIXEL_SIZE * COL_PER_PAGE)), start_y)
    turtle.goto((start_x - 80), start_y - 30)
    for i in range(6,9):
        start_x = turtle.xcor()
        start_y = turtle.ycor()
        pixel_list = image_list[i]
        draw_page(turtle, pixel_list)
        turtle.goto((start_x + (PIXEL_SIZE * COL_PER_PAGE)), start_y)
    turtle.goto((start_x - 80), start_y - 30)

    

def main():
    print("Welcome. Let me render an image for you!")
##    ask_image_size()
##    user_selection = collect_image_size(IMAGE_OPTIONS)
##
##    compressed_string = compress(user_selection)
##    decompressed_string = decompress(compressed_string)
##
    screen = turtle.Screen()
    screen.tracer(0)

    compress_img = compress(LITTLE_IMG)
    decompress_img = decompress(compress_img)
    draw = turtle.Turtle()
    draw.hideturtle()
    draw_image(draw, decompress_img)
    screen.update()

    

main()

# BECAUSE I'M NOT UNPAGINATING THE IMAGE, THESE WON'T WORK

##def determine_x_size(image_list, pixel_size):
##    ''' Name: determine_x_size
##        Input: nested list of strings (image_list) and pixel_size (int)
##        Returns: size of x axis of image in pixels (float)
##    '''
##    # len(image_list[0]) is called to determine number of columns/pixels
##    num_pixels = len(image_list[0])
##
##    x_size = num_pixels * pixel_size
##    return x_size
##
##def determine_y_size(original_list, PIXEL_SIZE):
##    '''
##        Does: returns verticle size of image (int)
##    '''
##    num_pixels = len(original_list)
##    y_size = num_pixels * PIXEL_SIZE
##    return y_size


# My want to fiddle with this...not need at all?
def setup_screen(screen_turtle, draw_turtle, original_list, PIXEL_SIZE):
    screen_turtle.tracer(0)
##    x_size = determine_x_size(original_list, PIXEL_SIZE)
##    y_size = determine_y_size(original_list, PIXEL_SIZE)
##    turtle.setup(x_size, y_size)

def determine_x_start(original_list, PIXEL_SIZE):
    '''
        Does: determines starting x cord based on pixel list and size
    '''
    x_size = determine_x_size(original_list, PIXEL_SIZE)
    x_cord = x_size / 2
    return x_cord

def determine_y_start(original_list, PIXEL_SIZE):
    '''
        Does: determines starting y cord based on pixel list and size
    '''
    y_size = determine_y_size(original_list, PIXEL_SIZE)
    y_cord = y_size / 2
    return y_cord
