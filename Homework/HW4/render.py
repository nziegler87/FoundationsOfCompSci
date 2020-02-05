'''
    Nathanial Ziegler
    CS 5001
    February 5, 2020
    HW 4
    Description:
        Ask user if they want to render a large or small image. Compresses the
        string of pixels for corresponding image. Then decompress and
        uses Turtle to render image on screen.        
'''

from render_images import *
from compress_functions import *
import turtle

# Image compression and rendering constants
ROW_PER_PAGE = 3
COL_PER_PAGE = 4
PIXEL_SIZE = 10
IMAGE_OPTIONS = ["BIG", "LITTLE"]

# Constants for draw_pixel function
SIDES_IN_SQUARE = 4
RIGHT_TURN = 90

def validate_input(user_input, option_list):
    ''' Name: validate_input
        Inputs: user_input, list of options both strings
        Returns: True if user_input is in list of options
        Does: Compares user_input to option list and returns True
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
    # Ask if user wants to render the BIG or LITTLE image
    selection = input("Enter BIG or LITTLE: ").upper()

    # Call validate input to ensure response is valid
    while not validate_input(selection, option_list):
        selection = input("You must enter either BIG or LITTLE. " + \
                          "Try again: ").upper()

    # Call input_to_file to return variable name
    file = input_to_file(selection)

    return file

def set_start_cord(draw_turtle, uncompressed_img, pixel_size, row_per_page,
                   col_per_page):
    ''' Name: set_start_cord
        Input: draw_turtle name, uncompressed image (nested list of strings),
               pixel_size (int)
        Returns: nothing
        Does: sets turtle to x, y cord so image is centered on page
    '''
    draw_turtle.up()

    # Calculate y cord using original image
    num_row = calculate_row_pages(uncompressed_img, row_per_page)
    y_size = num_row * row_per_page * pixel_size
    y_cord = y_size / 2

    # Calcuate x cord using original image 
    num_col = calculate_col_pages(uncompressed_img, col_per_page)
    x_size = num_col * col_per_page * pixel_size
    x_cord = x_size / 2
    
    draw_turtle.goto(-(x_cord),(y_cord))

def draw_pixel(turtle, color, pixel_size):
    ''' Name: draw_pixel
        Input: turtle name, color of turtle (str), pixel_size (int)
        Returns: nothing
        Does: Draws one "pixel" based on pixel size and color
    '''
    # Set turtle initial state; set to down incase not reaady to write
    turtle.hideturtle()
    turtle.down()
    turtle.color(color, color)
    turtle.begin_fill()

    # Iterate through four loop to make square
    for i in range(SIDES_IN_SQUARE):
        turtle.forward(pixel_size)
        turtle.right(RIGHT_TURN)

    # Fill pixel and prepare turtle for move
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
    for i in range(1, COL_PER_PAGE):
        start_x = turtle.xcor()
        start_y = turtle.ycor()
        
        # Render pixel for each row using pixel_to_color and draw_pixel functions
        while j < ((i * COL_PER_PAGE)):
            color = pixel_to_color(pixel_list[j])
            draw_pixel(turtle, color, PIXEL_SIZE)
            turtle.forward(10)
            j += 1

        # Move turtle to starting point but down a row of pixles
        turtle.goto(start_x, (start_y - PIXEL_SIZE))

def draw_image(turtle, image_list, num_row, num_col):
    ''' Name: draw_image
        Inputs: turtle, image_list (nested list of strings),
                num_row and num_col -- both ints
        Returns: nothing
    '''
    start_x = turtle.xcor()
    start_y = turtle.ycor()
    row = 1
    for page in range(len(image_list)):
        if page < (row * num_col):
            x_cord = turtle.xcor()
            y_cord = turtle.ycor()
            pixel_list = image_list[page]
            draw_page(turtle, pixel_list)
            turtle.goto((x_cord + (COL_PER_PAGE * PIXEL_SIZE), y_cord))
        else:
            turtle.goto((start_x), (y_cord - ROW_PER_PAGE * PIXEL_SIZE))
            x_cord = turtle.xcor()
            y_cord = turtle.ycor()
            pixel_list = image_list[page]
            draw_page(turtle, pixel_list)
            turtle.goto((x_cord + (COL_PER_PAGE * PIXEL_SIZE), y_cord))
            row += 1

def main():
    # Welcome user and ask for image to be rendered
    print("Welcome. Let me render an image for you!")
    ask_image_size()
    user_selection = collect_image_size(IMAGE_OPTIONS)

    # Calculate original image size
    page_per_row = calculate_row_pages(user_selection, ROW_PER_PAGE)
    page_per_col = calculate_col_pages(user_selection, COL_PER_PAGE)

    # Compress image for uploading and then decompress
    compressed_img = compress(user_selection)
    decompressed_img = decompress(compressed_img)

    # Setup turtle
    screen = turtle.Screen()
    screen.tracer(0)
    draw = turtle.Turtle()

    # Draw image
    set_start_cord(draw, user_selection, PIXEL_SIZE, ROW_PER_PAGE,
                   COL_PER_PAGE)
    draw_image(draw, decompressed_img, page_per_row, page_per_col)
    screen.update()

main()
