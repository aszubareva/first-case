# Case-study #1
# Developers:  Ufilin A.
#
import turtle as t #после написания процедуры черепаха смотрит вправо!!!
import math


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

def right_triangle (x, y, a, b, color):
    '''
    Function, drawing right_triangle.
    :param x: point between legs coordinate x
    :param y: point between legs coordinate y
    :param a: first leg lenght
    :param b: second leg lenght
    :param color: color of triangle
    :return: None
    '''
    t.up()
    t.setposition(x, y)
    t.down()
    t.color('black', color)
    t.begin_fill()
    t.forward(a)
    pos_a = t.pos()
    t.right(180)
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.goto(pos_a)
    t.right(90)
    t.end_fill()
    t.seth(0)

def circle (x, y, r, color):
    '''
    Function, drawing circle.
    :param x: centre point coordinate x
    :param y: centre point coordinate y
    :param r: radius of circle
    :param color: color of circle
    :return: None
    '''
    t.up()
    t.setposition(x, y)
    t.down()
    t.color('black', color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.seth(0)


def main():
    '''
    Main function.
    :return: None
    '''
    t.tracer(0)
    t.done()


main()
