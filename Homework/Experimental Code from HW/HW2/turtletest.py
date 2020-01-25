'''
    Nathanial Ziegler
    CS5003
    January 21, 2020
    Homework 2
    Description:
    [insert description
'''

import turtle, math

from boston import *

def main():
    screen = turtle.Screen()
    screen.setup(800, 365)
    screen.bgpic("boston_map.png")

    wvh = turtle.Turtle()
    wvh.hideturtle()
    
    draw_circle(wvh, "Light Blue")

    label_circle(wvh, "WVH")

    user_place = input("What is your favorite place near Northeastern? ")
    user_lat = float(input("What is the latitude of this place? "))
    user_long = float(input("What is the longitude of this place? "))
    user_color = input("What primary color do you want to use for this place? ")

    y = lat_conversion(user_lat)
    x = long_conversion(user_long)

    favorite_place = turtle.Turtle()
    favorite_place.hideturtle()
    favorite_place.up()
    favorite_place.goto(x, y)
    favorite_place.down()

    draw_circle(favorite_place, user_color)
    
    

main()
