COOKIE = "cc_cookie.gif"
BG_COLOR = "Light Grey"

def setup_turtle(turtle, turtle_screen):
    ''' Name: setup_screen
        Input: turtle and turtle_screen variables
        Returns: nothing
    '''
    turtle_screen.addshape(COOKIE)
    turtle_screen.bgcolor(BG_COLOR)
    turtle.shape(COOKIE)
