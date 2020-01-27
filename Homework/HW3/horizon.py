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

def main():

    # Set screen and initial canvas color
    screen = turtle.Screen()
    screen.setup(SCREEN_SIZE, SCREEN_SIZE)
    screen.bgcolor("#C9EEFF")
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
    sun.setpos(150, 200)
    sun.shape(sun_gif)

    # Create moon turtle
    moon = turtle.Turtle()
    moon.speed(0)
    moon.up()
    moon.setpos(-475, 200)
    moon.shape(moon_gif)

    # Animation loop
    while True:
        screen.update()
        # Stop animation once moon is off the screen
        if moon.xcor() == ((SCREEN_SIZE / 2) + MOON_RADIUS):
            break
        # Increment sun forward. Change background color when moon and sun overlap
        if moon.xcor() <= (sun.xcor() - SUN_RADIUS) or moon.xcor() >= (sun.xcor() + SUN_RADIUS):
            screen.bgcolor("#C9EEFF")
            moon.forward(5)
        else:
            screen.bgcolor("#738993")
            moon.forward(5)
            
main()
