# Tegn_figur_4
import turtle

def tegn_figur(sider, color):

    turtle.color(color)

    for i in range(0, sider):
        turtle.fd(50)
        turtle.lt(360/sider)
    turtle.fd(100)

turtle.penup()
turtle.goto(-250,0)
turtle.pendown()

tegn_figur(4,'blue')
tegn_figur(3,'red')
tegn_figur(5, 'green')
tegn_figur(6, 'orange')

delay = input('Tryk på stop for at standse')