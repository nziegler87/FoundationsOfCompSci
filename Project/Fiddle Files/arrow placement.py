import turtle

y = 200

for i in range(1, 5):
    name = "turtle - " + str(i)
    name = turtle.Turtle()
    name.up()
    name.sety(y)
    name.down()
    name.circle(10)
    name.hideturtle()
    y -= 50
    
