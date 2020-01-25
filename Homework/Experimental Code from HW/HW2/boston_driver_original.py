'''
    Nathanial Ziegler
    CS 5001
    Homework 2
    January 21, 2020
    Description:
        Displays a map of Boston with West Village H (WVH) as the center.
        User is asked for their favorite location in boston plus the lat / long of that
        place. A pin is then placed on the map at the location. The distance
        from that location to WVH is displayed
'''

from boston import *

def main():
    # Set turtle canvas size and loads background image
    screen = turtle.Screen()
    screen.setup(800, 565)
    screen.bgpic("boston_map.png")

    # Circle and label WVH on map
    wvh = turtle.Turtle()
    wvh.hideturtle()
    draw_circle(wvh, "Light Green")
    label_circle(wvh, "WVH")

    # Collect information about user's favorite place
    user_place = input("What is your favorite place near Northeastern? ")
    user_lat = float(input("What is the latitude of this place? "))
    user_long = float(input("What is the longitude of this place? "))
    user_color = input("Your location will be assigned a pin on the map.\n" +
                       "What color do you want this pin to be? ")

    # Convert user inputed lat, long and calculate distance to WVH
    y = convert_lat(user_lat)
    x = convert_long(user_lat, user_long)
    distance = calc_distance(user_lat, user_long)

    # Set new turtle to user-entered coordinates
    favorite_place = turtle.Turtle()
    favorite_place.hideturtle()
    favorite_place.up()
    favorite_place.goto(x, y)
    favorite_place.down()

    # Draw circle with user x,y coord as center then label
    pin_label = user_place + "\n" + str(round(distance, 3))
    draw_circle(favorite_place, user_color)
    label_circle(favorite_place, pin_label)

main()
