import turtle

def draw_square(a_turtle, side):
    for i in range(4):
        a_turtle.forward(side)
        a_turtle.right(90)

def nested_square(a_turtle, side):
    if side >= 1:
        draw_square(a_turtle, side)
        nested_square(a_turtle, side - 5)

def centered_square(a_turtle, x_cord, y_cord, side_length):
    a_turtle.speed(0)
    a_turtle.hideturtle()
    a_turtle.up()
    a_turtle.setpos(x_cord - (side_length/2), y_cord + (side_length/2))
    a_turtle.down()
    for i in range(4):
        a_turtle.forward(side_length)
        a_turtle.right(90)

def nested_center_squares(a_turtle, x_cord, y_cord, side_length):
    if side_length >= 1:
        centered_square(a_turtle, x_cord, y_cord, side_length)
        nested_center_squares(a_turtle, x_cord, y_cord, side_length - 11)

square = turtle.Turtle()

nested_center_squares(square, 0, 0, 200)



##nested_square(square, 200)
