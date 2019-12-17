# Fremstil seperate funktioner for kvadrater og trekandter
import turtle

def tegn_kvadrat():
    for i in range(0, 4):
        turtle.fd(50)
        turtle.lt(90)
    turtle.fd(100)

def tegn_trekandt():
    for i in range(0, 3):
        turtle.fd(50)
        turtle.lt(120)
    turtle.fd(100)

turtle.penup()
turtle.goto(-250,0)
turtle.pendown()

tegn_kvadrat()
tegn_trekandt()
tegn_kvadrat()
tegn_trekandt()

delay = input('Tryk på stop for at standse')