import turtle

def get_location(x, y):
    print("X CORD:", x, "\nY CORD:", y, "\n\n")

screen = turtle.Screen()
yellow = turtle.Turtle()
red = turtle.Turtle()
white = turtle.Turtle()

yellow_piece = "./images/yellow_piece_90.gif"
red_piece = "./images/red_piece_90.gif"
white_piece = "./images/white_piece_90.gif"

screen.addshape(yellow_piece)
screen.addshape(red_piece)
screen.addshape(white_piece)
screen.bgcolor("blue")
screen.tracer(0)

white.up()
white.hideturtle()
yellow.up()
yellow.hideturtle()
red.up()
red.hideturtle()

yellow.shape(yellow_piece)
red.shape(red_piece)
white.shape(white_piece)

count = 0
piece_dict = {}
for x in range(250, -300, -100):
    for y in range(-275, 276, 100):
        white.goto(y, x)
        piece_dict[count] = white.stamp(), white.pos()
        white.write(count, align = "center", font = ("arial", 14, "bold"))
        count += 1

screen.update()

turn = ""



if turn == "yellow":
    turn = "red"
else:
    turn = "yellow"
    
for location in piece_dict.keys():
    
    x, y = piece_dict[location][1]

    if turn == "red":
        red.showturtle()
        red.goto(x, y)
        red.stamp()
    else:
        yellow.showturtle()
        yellow.goto(x, y)
        yellow.stamp()

    screen.update()

while True:

    if turn == "yellow":
        turn = "red"
    else:
        turn = "yellow"
        
    for location in piece_dict.keys():
        
        x, y = piece_dict[location][1]

        if turn == "red":
            yellow.clear()
            red.showturtle()
            red.goto(x, y)
            red.stamp()
        else:
            red.clear()
            yellow.showturtle()
            yellow.goto(x, y)
            yellow.stamp()

        screen.update()

        if turn == "yellow":
            turn = "red"
        else:
            turn = "yellow"
