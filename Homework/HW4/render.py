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
        Input: nothing
        Return
    '''
    if user_selection == "BIG":
        return BIG_IMG
    else:
        return LITTLE_IMG

def collect_image_size(option_list):
    ''' Name: collect_image_size
        Input:
        Returns:
    '''
    selection = input("Enter BIG or LITTLE: ").upper()
    while not validate_input(selection, option_list):
        selection = input("You must enter either BIG or LITTLE. " + \
                          "Try again: ").upper()
    file = input_to_file(selection)
    return file

def setup_screen(turtle):
    turtle.tracer(0)

def draw_pixel(turtle, color, PIXEL_SIZE):
    turtle.hideturtle()
    turtle.down()
    turtle.color(color, color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
    turtle.end_fill()
    turtle.up()

def pixel_to_color(pixel):
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
    start_x = turtle.xcor()
    start_y = turtle.ycor()
    for row in range(3):
        for col in range(4):          
            col_mult = col * 4
            for i in range(len(pixel_list)):
                color = pixel_to_color(pixel_list[j])
                draw_pixel(turtle, color, PIXEL_SIZE)
                turtle.forward(10)
        
def decompress(compressed_list):
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
    print(decompressed_list)
    

def main():
    print("Welcome. Let me render an image for you!")
##    ask_image_size()
##    user_selection = collect_image_size(IMAGE_OPTIONS)
##
##    string = compress(user_selection)
##
##    print(string)
##
##    screen = turtle.Screen()
##    setup_screen(screen)
##    draw = turtle.Turtle()

    

main()
