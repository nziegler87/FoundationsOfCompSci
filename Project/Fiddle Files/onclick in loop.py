from turtle import Screen, Turtle

WIDTH, HEIGHT = 1200, 1500

dict_alunos = {'joao': ['5', 'm'], 'maria': ['5', 'm'], 'lobo': ['5', 'm'], 'mau': ['5', 'm']}

def text(t, text, size, color, x, y):
    t.penup()
    t.goto(x + size, y - size/2)
    t.color(color)
    t.write(text, align='left', font=('Arial', str(size), 'normal'))
    t.goto(x, y)

def caca(dictionary, mes):

    def tnome_handler(nome, turtle, x, y):

        pnt = screen.textinput('pontuação', '%s:  ' % (nome))
        pnt = [int(x) for x in pnt.split()]

        if len(pnt) == 5:
            with open('%s.py' % (mes), 'a') as fd:
                fd.write('s.pontuacao(%i, %i, %i, %i, %i)\n' % (nome, pnt[0], pnt[1], pnt[2], pnt[3], pnt[4]))

        turtle.color('blue')

    vert = 350
    hor = -600

    new_vert = vert

    for nome in dictionary:

        if vert == -340:
            new_vert = 350
            new_hor = hor + 250

        if vert != -340:
            new_vert = new_vert - 30
            new_hor = hor
            txt_vert = new_vert - 15
            txt_hor = new_hor + 20

        turtle = Turtle(shape='turtle')
        turtle.color('pink')
        turtle.speed('fastest')
        turtle.setheading(0)

        text(turtle, '%s' % (nome), 20, 'pink', txt_hor, txt_vert)

        turtle.onclick(lambda x, y, n=nome, t=turtle: tnome_handler(n, t, x, y))

screen = Screen()
screen.setup(WIDTH, HEIGHT)

caca(dict_alunos, 'mm')

screen.mainloop()
