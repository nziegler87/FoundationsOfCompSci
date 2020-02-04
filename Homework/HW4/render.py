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
PIXEL_SIZE = 10
IMAGE_OPTIONS = ["BIG", "LITTLE"]

from render_images import *
from compress_functions import *
import turtle

def validate_input(user_input, option_list):
    ''' Name: validate_input
        Inputs: user_input, list of options
        Returns: True of user_input is in list of options
        Does: Compares user_input to two options and returns True
              if user_input matches one of the responses.
    '''
    if user_input in option_list:
        return True

def ask_image_size():
    ''' Name: ask_image_size
        Input: nothing
        Returns: nothing
    '''
    print("Do you want me to render a big or small image?")

def input_to_file(user_selection):
    ''' Name: input_to_file
        Input: user selection as a string
        Return: file name variable based on user input
        Does: returns BIG_IMG if user enters "BIG" or LITTLE_IMG if
              user enters "LITTLE"
    '''
    if user_selection == "BIG":
        return BIG_IMG
    else:
        return LITTLE_IMG

def decompress(compressed_list):
    '''
        Does: decompresses pixel list
    '''
    decompressed_list = []
    for i in range(len(compressed_list)):
        page_list = []
        for j in range(len(compressed_list[i])):
            item = compressed_list[i][j].split(" ")
            number = int(item[0])
            pixel = item[1]
            for num in range(number):
                page_list.append(pixel)
        decompressed_list.append(page_list)
    return(decompressed_list)

def collect_image_size(option_list):
    ''' Name: collect_image_size
        Input: list of user options, each as string
        Returns: name of file to be generated
    '''
    selection = input("Enter BIG or LITTLE: ").upper()
    while not validate_input(selection, option_list):
        selection = input("You must enter either BIG or LITTLE. " + \
                          "Try again: ").upper()
    file = input_to_file(selection)
    return file

def determine_x_size(original_list, PIXEL_SIZE):
    '''
        Does: returns horizontal size of image (int)
    '''
    num_pixels = len(original_list[0])
    x_size = num_pixels * PIXEL_SIZE
    return x_size

def determine_y_size(original_list, PIXEL_SIZE):
    '''
        Does: returns verticle size of image (int)
    '''
    num_pixels = len(original_list)
    y_size = num_pixels * PIXEL_SIZE
    return y_size

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

def set_start_cord(draw_turtle, original_list, PIXEL_SIZE):
    '''
        Does: sets turtle to render pixels at starting cord,
              based on pixel list and size
    '''
    draw_turtle.up()
    y_cord = determine_y_start(original_list, PIXEL_SIZE)
    x_cord = determine_x_start(original_list, PIXEL_SIZE)
    draw_turtle.goto(-(x_cord),(y_cord))

def draw_pixel(turtle, color, PIXEL_SIZE):
    turtle.down()
    turtle.color(color, color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
    turtle.end_fill()
    turtle.up()

def pixel_to_color(pixel):
    '''
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
    '''
        Does: Draws one page of pixels
    '''
    i = 0
    for j in range(1, 4):
        start_x = turtle.xcor()
        start_y = turtle.ycor()
        while i < ((j * 4)):
            color = pixel_to_color(pixel_list[i])
            draw_pixel(turtle, color, PIXEL_SIZE)
            turtle.forward(10)
            i += 1
        turtle.goto(start_x, (start_y - PIXEL_SIZE))
               
def draw_image(turtle, image_list):
    image_col = calculate_col(image_list, COL_PER_PAGE)
    print("Image col: ", image_col)
    image_row = calculate_row(image_list, ROW_PER_PAGE)
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
##    setup_screen(screen)

    LITTLE_IMG = [[L, L, L, L, R, R, R, R, L, L, L, L],
                  [L, L, L, R, R, R, R, R, R, L, L, L],
                  [L, L, L, O, O, Y, Y, B, Y, L, L, L],
                  [L, L, O, Y, B, Y, Y, B, Y, Y, Y, L],
                  [L, L, O, Y, B, Y, Y, Y, B, Y, Y, Y],
                  [L, L, L, O, Y, Y, Y, B, B, B, B, L],
                  [L, L, L, L, Y, Y, Y, Y, Y, L, L, L],
                  [L, L, L, R, R, L, R, R, L, R, L, L],
                  [L, L, R, R, R, L, R, R, L, R, R, L]]
    compress_img = compress(LITTLE_IMG)
    decompress_img = decompress(compress_img)
    draw = turtle.Turtle()
    draw.hideturtle()
    draw_image(draw, decompress_img)
    screen.update()

    

main()
