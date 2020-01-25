def drawSquare (myTurtle, sideLength):
    myTurtle.forward(sideLength)
    myTurtle.right(90)
    myTurtle.forward(sideLength)
    myTurtle.right(90)
    myTurtle.forward(sideLength)
    myTurtle.right(90)
    myTurtle.forward(sideLength)
    myTurtle.right(90)

def drawSpiral (myTurtle, maxAngel):
    for angel in range(0, maxAngel + 1, 2):
        myTurtle.forward(10)
        myTurtle.right(angel)

def draw10Squares (myTurtle):
    for i in range (200, 200 - 10 * 10, -10):
        drawSquare(myTurtle, i)
        
    
            

