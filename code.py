import turtle as t
import math
t.tracer(0)
#после написания процедуры черепаха смотрит вправо!!!
def trapezoid ():
    pass


def rectangle(x, y, sidea, sideb, colour_edge = "black", colour_fill = "white", rotation = 0):
    # если фигура не повернута, то side a - нижняя и верхняя сторона, а side b - левая и правая.
    # rotation - угол поворота фигуры на rotation градусов, угол между Ох и нижней стороной прямоугольника.
    t.up()
    t.goto(x, y)
    t.down()
    t.left(rotation)
    t.color(colour_edge)
    t.fillcolor(colour_fill)
    t.begin_fill()
    for _ in range(2):
        t.forward(sidea)
        t.left(90)
        t.forward(sideb)
        t.left(90)
    t.end_fill()
    t.setheading(0)
    t.color("black")

def rhomb(x, y, side, angle, colour_edge = "black", colour_fill = "white", rotation = 0):
    # rotation - угол поворота фигуры на rotation градусов, угол между Ох и нижней стороной ромба.
    # angle - меньший из внутренних углов ромба (т.е. 0 <= angle <= 90). Если ромб не повернут, то это угол между нижней и левой стороной ромба
    t.up()
    t.goto(x, y)
    t.down()
    t.left(rotation)
    t.color(colour_edge)
    t.fillcolor(colour_fill)
    t.begin_fill()
    for _ in range(2):
        t.forward(side)
        t.left(angle)
        t.forward(side)
        t.left(180 - angle)
    t.end_fill()
    t.setheading(0)
    t.color("black")



t.done()


