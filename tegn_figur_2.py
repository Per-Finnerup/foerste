# Tegn_figur_2
import turtle

def tegn_figur(figur):
    if figur == 'kvadrat':
        for i in range(0, 4):
            turtle.fd(50)
            turtle.lt(90)
        turtle.fd(100)

    if figur == 'trekandt':
        for i in range(0, 3):
            turtle.fd(50)
            turtle.lt(120)
        turtle.fd(100)

turtle.penup()
turtle.goto(-250,0)
turtle.pendown()

tegn_figur('kvadrat')
tegn_figur('trekandt')
tegn_figur('kvadrat')
tegn_figur('trekandt')

delay = input('Tryk på stop for at standse')