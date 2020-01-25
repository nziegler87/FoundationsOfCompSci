
import turtle

nate = turtle.Turtle()

##count = 500
##
##for x in range (500, -1, -5):
##    if count % 2 == 0:
##        nate.dot(x, "black")
##        count -= 1
##    else:
##        nate.dot(x, "white")
##        count -= 1

nate.color("blue")
y = 0
nate.speed(0)

for x in range (90):
    nate.right(y)
    nate.forward(250)
    nate.up()
    nate.setpos(0, 0)
    nate.down()
    y =+ 4

nate.color("orange")
y = 1

for x in range (90):
    nate.right(y)
    nate.forward(250)
    nate.up()
    nate.setpos(0, 0)
    nate.down()
    y =+ 4

nate.color("purple")
y = 2

for x in range (90):
    nate.right(y)
    nate.forward(250)
    nate.up()
    nate.setpos(0, 0)
    nate.down()
    y =+ 4

nate.color("green")
y = 3

for x in range (90):
    nate.right(y)
    nate.forward(250)
    nate.up()
    nate.setpos(0, 0)
    nate.down()
    y =+ 4
