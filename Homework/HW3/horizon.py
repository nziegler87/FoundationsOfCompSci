'''
    Nathanial Ziegler
    CS 5001
    January 29, 2020
    HW 3
    Description:
        Animation of moon moving across screen. When then moon overlaps with
        the sun, the background turns dark. Animation stops when moon
        is off screen.

    Referenced:
        https://learn.wecode24.com/animation-with-turtle-graphics/
        https://automatetheboringstuff.com/chapter8/
'''

import turtle

# Constants for functions
SUN_RADIUS = 100
MOON_RADIUS = 100
SCREEN_SIZE = 800
Y_CORD = 200
MOON_X_CORD = -475
SUN_X_CORD = 150
DAYLIGHT_SKY = "#C9EEFF"
ECLIPSE_SKY = "#738993"
TRACER_REFRESH = 0
TURTLE_DRAW_SPEED = 0
ANIMATION_SPEED = 3

# Images for turtles
SUN_GIF = "./images/sun.gif"
MOON_GIF = "./images/moon.gif"

def turtle_setup(turtle, draw_speed, x_cord, y_cord, image):
    ''' Name: turtle_setup
        Input: turtle (variable), draw_speed (int), x_cord & y_cord (float),
               image (string or var)
        Return: nothing
        Does: Sets starting location, animiation speed, and image
              for turtle
    '''
    turtle.speed(draw_speed)
    turtle.up()
    turtle.setpos(x_cord, y_cord)
    turtle.shape(image)

def screen_setup(turtle, x_dimension, y_dimension, bg_color, refresh_rate):
    ''' Name: screen_setup
        Input: turtle (variable), x_dimension and y_dimension (floats),
               bg_color (string), refresh_rate (int)
        Return: nothing
        Does: Sets initial screen settings: size, color, and refresh time rate
    '''
    turtle.setup(x_dimension, y_dimension)
    turtle.bgcolor(bg_color)
    turtle.tracer(refresh_rate)

def main():
    # Set screen and initial canvas color
    screen = turtle.Screen()
    screen_setup(screen, SCREEN_SIZE, SCREEN_SIZE, DAYLIGHT_SKY, TRACER_REFRESH)

    # Add sun and moon shapes
    screen.addshape(SUN_GIF)
    screen.addshape(MOON_GIF)

    # Create sun turtle
    sun = turtle.Turtle()
    turtle_setup(sun, TURTLE_DRAW_SPEED, SUN_X_CORD, Y_CORD, SUN_GIF)

    # Create moon turtle
    moon = turtle.Turtle()
    turtle_setup(moon, TURTLE_DRAW_SPEED, MOON_X_CORD, Y_CORD, MOON_GIF)

    # Animation loop
    while True:
        moon.forward(ANIMATION_SPEED)
        screen.update()

        # Stop animation once moon is off the screen
        if moon.xcor() > ((SCREEN_SIZE / 2) + MOON_RADIUS):
           screen.bye()

        # Increment sun forward; change background color when moon and sun overlap
        elif moon.xcor() <= (sun.xcor() - SUN_RADIUS) or moon.xcor() >= (sun.xcor() + SUN_RADIUS):
            screen.bgcolor(DAYLIGHT_SKY)
        else:
            screen.bgcolor(ECLIPSE_SKY)
            
main()
