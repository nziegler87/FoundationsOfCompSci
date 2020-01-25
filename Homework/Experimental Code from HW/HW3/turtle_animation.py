'''
    Nathanial Ziegler
    CS 5001
    January 25, 2020
    HW 3
    Description:
        Experimenting with turtle animation.
'''

import turtle

def draw_square(turtle):
    for side in range(4):
        turtle.forward(100)
        turtle.left(90)

def main():

    screen = turtle.Screen()
    screen.setup(500, 500)
    screen.tracer(0)

    don = turtle.Turtle()
    don.speed(0)
    don.hideturtle()

    don.penup()
    don.goto(-350, 0)
    don.pendown()

    while True:
        don.clear()
        draw_square(don)
        screen.update()
        don.forward(1)

main()
