'''
    CS 5001
    Nathanial Ziegler
    February 5, 2020
    HW 3
    Description:
        UPDATE
'''

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

def draw_pixel(turtle, screen, color, size):
    turtle.hideturtle()
    turtle.color(color, color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
    screen.update()

##def draw_page(turtle, screen, color, size, pixel_list):
    

def main():
    print("Welcome. Let me render an image for you!")
    ask_image_size()
    user_selection = collect_image_size(IMAGE_OPTIONS)

    string = compress(user_selection)

    print(string)

##    screen = turtle.Screen()
##    setup_screen(screen)
##    draw = turtle.Turtle()
##    draw_pixel(draw, screen, "light blue", 10)
    

main()
