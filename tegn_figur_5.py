# Tegn_figur_5
import turtle

# definer konstanter
TREKANDT = 3
FIRKANDT = 4
FEMKANDT = 5
HEKSAGON = 6
SYVKANDT = 7
def tegn_figur(sider, color):

    turtle.color(color)

    for i in range(0, sider):
        turtle.fd(50)
        turtle.lt(360/sider)
    turtle.fd(100)

turtle.penup()
turtle.goto(-250,0)
turtle.pendown()

tegn_figur(TREKANDT,'blue')
tegn_figur(FIRKANDT,'red')
tegn_figur(FEMKANDT, 'green')
tegn_figur(HEKSAGON, 'orange')
tegn_figur(SYVKANDT, 'orange')

delay = input('Tryk på stop for at standse')