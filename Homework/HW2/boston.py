'''
    Nathanial Ziegler
    CS5001
    Homework 2
    January 21, 2020
    Description:
        Functions needed for boston_driver to operate:
            convert_lat
            convert_long
            calc_distance
            place_pin
            draw_line
            move_turtle
'''
import turtle, math

# Background map image
BACKGROUND_IMAGE = "boston_map.png"
IMAGE_X = 800
IMAGE_Y = 565

# Images used for map pins
BLUE_PIN = "map_pin_blue.gif"
YELLOW_PIN = "map_pin_yellow.gif"

# WVH coords used as x = 0, y = 0 for conversion and distance calc functions
LAT0 = 42.338574
LONG0 = -71.0945489

# Global Variables for conversion equations
# Don't fully understand lat, long, dist eqs; doing my best with variable names
PI = 3.14
MAP_DIMENSION = 4000000
DEGREES_IN_SPHERE = 360
EUCLIDEAN_CONSTANT = 110.25

# Label formatting constants
LABEL_FONT = "Arial"
LABEL_FONT_SIZE = 10
LABEL_FONT_STYLE = "bold"
LABEL_OFFSET = 15
VERTICLE_ADJUST = 3

def convert_lat(LAT0, lat):
    ''' Inputs: LAT0 and lat coordinates (floats)
        Returns: y coordinate (float)
        Does: Calculates y coordinate using global LAT0 variable and
              user inputed latitude
    '''    
    y = ((lat - LAT0) * MAP_DIMENSION) / DEGREES_IN_SPHERE
    
    return y

def convert_long(LAT0, LONG0, lat, long):
    ''' Inputs: LAT0, LONG0, lat, and long (floats)
        Returns: x coordinate (float)
        Does: Calculates x coordinate using global LAT0 and LONG0 variables
              and user inputed latitude and longitude
    '''
    x = math.cos((lat + LAT0) * PI / DEGREES_IN_SPHERE)
    x = (long - LONG0) * MAP_DIMENSION * x
    x = x / DEGREES_IN_SPHERE

    return x

def calc_distance(LAT0, LONG0, lat, long):
    ''' Inputs: Latitude and longitude coordinates (floats)
        Returns: Distance (float)
        Does: Calculates distance from user-entered Lat, Long coordinates
              to LAT0, LONG0
    '''
    distance = ((long - LONG0) * math.cos(LAT0))**2
    distance = (lat - LAT0)**2 + distance
    distance = math.sqrt(distance)
    distance = EUCLIDEAN_CONSTANT * distance
    
    return distance

def place_pin(turtle, label, image):
    ''' Inputs: Turtle name variable, label (string), image file path (string)
        Returns: Nothing
        Does: Puts an image pin at set coordinates and adds label
    '''
    # Gets current turtle position
    x = turtle.xcor()
    y = turtle.ycor()

    # Lift up turtle pen so line is not drawn as it is moved around screen
    turtle.up()

    # Moves turtle so that bottom of pin is flush with x, y coordinates
    turtle.goto(x, y + LABEL_OFFSET)

    # Stamps turtle image on map
    turtle.shape(image)
    turtle.stamp()
    turtle.hideturtle()

    # Returns turtle to original x, y coord
    turtle.goto(x, y)

    # Moves turtle so that text does not overlap with pin
    turtle.goto(x + LABEL_OFFSET, y)

    # Writes label with specified font
    turtle.write(label, font=(LABEL_FONT, LABEL_FONT_SIZE, LABEL_FONT_STYLE))

    # Returns turtle to original x, y coord 
    turtle.goto(x, y)

def draw_line(begin_turtle, end_turtle):
    ''' Inputs: begin_turtle and end_turtle names
        Returns: Nothing
        Does: Draws line between starting and end turtles
    '''
    # Gets coordinates of starting turtle
    x = begin_turtle.xcor()
    y = begin_turtle.ycor()

    # Moves starting point to bottom of marker pin
    begin_turtle.up()
    begin_turtle.goto(x, y - VERTICLE_ADJUST)
    begin_turtle.down()

    # Gets coordinates of ending turtle 
    x = end_turtle.xcor()
    y = end_turtle.ycor()

    # Draws line to bottom of home point pin
    begin_turtle.goto(x, y - VERTICLE_ADJUST)

def move_turtle(turtle, x_coord, y_coord):
    ''' Inputs: turtle name, and x, y coordinates (floats)
        Returns: Nothing
        Does: Moves specified turtle to x, y coordinates with turtle
              up so that a line is not drawn when moved
    '''
    turtle.up()
    turtle.goto(x_coord, y_coord)
    turtle.down()
