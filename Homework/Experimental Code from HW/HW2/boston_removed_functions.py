'''
    Nathanial Ziegler
    CS5001
    Homework 2
    January 21, 2020
    Description:
        Functions removed from original boston.py file: draw_circle and
        label_circle
'''

import turtle, math

# Default circle radius used in functions to draw labels on map
CIRCLE_RADIUS = 10

def draw_circle(turtle, fill_color):
    ''' Inputs: Turtle name and fill color (string)
        Returns: Nothing
        Does: Draws a circle around current coordinates as center and
              the circle is then filled with user-specified color
    '''
    # Gets current turtle position
    x = turtle.xcor()
    y = turtle.ycor()

    # Sets fill color
    turtle.fillcolor(fill_color)

    # Moves turtle so that drawn circle uses x, y coords as center point
    turtle.up()
    turtle.sety(y - CIRCLE_RADIUS)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(CIRCLE_RADIUS)
    turtle.end_fill()

    # Moves turtle back to original x, y coord
    turtle.up()
    turtle.goto(x, y)

def label_circle(turtle, label):
    ''' Inputs: Turtle name and label (string)
        Returns: Nothing
        Does: Labels current circle given entered label
    '''
    # Gets current turtle position
    x = turtle.xcor()
    y = turtle.ycor()

    # Moves turtle so that text does not overlap with circle
    turtle.goto(x + CIRCLE_RADIUS + 5, y - 5)

    # Writes label with specified font
    turtle.write(label, font=("Arial", 10, "bold"))

    # Returns turtle to original x, y coord 
    turtle.goto(x, y)
