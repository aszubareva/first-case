# Case-study #1
# Developers:  
#

import turtle #после написания процедуры черепаха смотрит вправо!!!
import math 


def trapezoid ():
    pass

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
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('black', color)
    turtle.begin_fill()
    turtle.forward(a)
    pos_a = turtle.pos()
    turtle.right(180)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.goto(pos_a)
    turtle.right(90)
    turtle.end_fill()
    turtle.seth(0)

def circle (x, y, r, color):
    '''
    Function, drawing circle.
    :param x: centre point coordinate x
    :param y: centre point coordinate y
    :param r: radius of circle
    :param color: color of circle
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('black', color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.seth(0)


def main():
    '''
    Main function.
    :return: None
    '''
    turtle.tracer(0)
    turtle.done()


main()
