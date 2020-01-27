'''
    Nathanial Ziegler
    CS 5001
    January 28, 2020
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
 
SUN_RADIUS = 100
MOON_RADIUS = 100
SCREEN_SIZE = 800
Y_CORD = 200
MOON_X_CORD = -475
SUN_X_CORD = 150
DAYLIGHT_SKY = "#C9EEFF"
ECLIPSE_SKY = "#738993"
ANIMATION_SPEED = 3

def main():

    # Set screen and initial canvas color
    screen = turtle.Screen()
    screen.setup(SCREEN_SIZE, SCREEN_SIZE)
    screen.bgcolor(DAYLIGHT_SKY)
    screen.tracer(0)

    # Add sun and moon shapes
    sun_gif = "./images/sun.gif"
    moon_gif = "./images/moon.gif"
    screen.addshape(sun_gif)
    screen.addshape(moon_gif)

    # Create sun turtle
    sun = turtle.Turtle()
    sun.speed(0)
    sun.up()
    sun.setpos(SUN_X_CORD, Y_CORD)
    sun.shape(sun_gif)

    # Create moon turtle
    moon = turtle.Turtle()
    moon.speed(0)
    moon.up()
    moon.setpos(MOON_X_CORD, Y_CORD)
    moon.shape(moon_gif)

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
