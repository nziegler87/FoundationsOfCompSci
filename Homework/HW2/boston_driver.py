'''
    Nathanial Ziegler
    CS 5001
    Homework 2
    January 21, 2020
    Description:
        Displays a map of Boston with West Village H (WVH) as the center.
        User is asked for their favorite location near Northeastern and
        the latitude / longitude of that location. A pin is then placed
        on the map at the location. The distance from that location to WVH
        is displayed and a line is drawn between the two points.

    Consulted:
        https://blog.trinket.io/using-images-in-turtle-programs/
        https://stackoverflow.com/questions/30426500/cant-add-shape-image
'''

from boston import *

import turtle

def main():
    # Set turtle canvas size and load background image
    screen = turtle.Screen()
    screen.setup(IMAGE_X, IMAGE_Y)
    screen.bgpic(BACKGROUND_IMAGE)
    
    # Register turtle images used for this program
    screen.addshape(BLUE_PIN)
    screen.addshape(YELLOW_PIN)

    # Label WVH on map with pin
    wvh = turtle.Turtle()
    wvh.hideturtle()
    place_pin(wvh, "WVH", BLUE_PIN)

    # Collect information about user's favorite place
    user_place = input("What is your favorite place near Northeastern? ")
    user_lat = float(input("What is the latitude of this place? "))
    user_long = float(input("What is the longitude of this place? "))

    # Convert user inputed lat, long and calculate distance to WVH
    y = convert_lat(LAT0, user_lat)
    x = convert_long(LAT0, LONG0, user_lat, user_long)
    distance = calc_distance(LAT0, LONG0, user_lat, user_long)

    # Set new turtle to user-entered coordinates
    favorite_place = turtle.Turtle()
    favorite_place.hideturtle()
    move_turtle(favorite_place, x, y)

    # Label favorite place on map with distance to WVH
    pin_label = user_place + "\n" + str(round(distance, 2)) + \
                " mile(s) from WVH"
    place_pin(favorite_place, pin_label, YELLOW_PIN)

    # Draws line from favorite place to WVH
    draw_line(favorite_place, wvh)

main()
