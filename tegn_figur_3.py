# Tegn_figur_3
import turtle

def tegn_figur(figur, color):

    turtle.color(color)
    if figur == 'kvadrat':
        for i in range(0, 4):
            turtle.fd(50)
            turtle.lt(90)
        turtle.fd(100)

    turtle.penup()
turtle.goto(-250,0)
turtle.pendown()

tegn_figur('kvadrat','blue')
tegn_figur('trekandt','red')
tegn_figur('kvadrat', 'green')
tegn_figur('trekandt', 'orange')

delay = input('Tryk på stop for at standse')