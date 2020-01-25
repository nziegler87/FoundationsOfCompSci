'''
    Nathanial Ziegler
    CS 5001
    January 28, 2020
    HW 3
    Description:
        Animation of moon moving across screen. When then moon overlaps with
        the sun, the background turns dark.

    Referenced:
        https://learn.wecode24.com/animation-with-turtle-graphics/
        https://automatetheboringstuff.com/chapter8/
'''

import turtle

def main():

    # Set screen and initial canvas color
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("#C9EEFF")

    # Add sun and moon shapes
    sun_gif = screen.addshape("./images/sun.gif")

    # Create sun turtle
    sun = turtle.Turtle()
    sun.shape(sun_gif)

main()
