import turtle

def tree(t, trunk_length):
    if trunk_length < 5:
        return
    else:
        print("Moving forward", trunk_length)
        t.forward(trunk_length)
        print("Turning right 30")
        t.right(30)
        print("Entering recursive call")
        tree(t, trunk_length - 5)
        print("Turning left 60")
        t.left(60)
        print("Entering second recursive call")
        tree(t, trunk_length - 5)
        print("Turning right 30")
        t. right(30)
        print("Heading back", trunk_length)
        t.backward(trunk_length)


t = turtle.Turtle()
turtle.speed(1)
t.up()
t.goto(0, -225)
t.down()
t.color("green", "green")
t.left(90)
tree(t, 15)
t.hideturtle()
