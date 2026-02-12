# Case-study #1
# Developers:  Ufilin A., Zubareva A., Berdyshev A.,
#
import turtle as t #после написания процедуры черепаха смотрит вправо!!!
import math


def isosceles_trapezoid(x, y, base1, base2, height, color, rotation):
    '''
    Function, drawing isosceles_trapezoid
    :param x: lower left corner coordinate x
    :param y: lower left corner coordinate y
    :param height: height of trapezoid
    :param base1: lower base length
    :param base2: upper base length
    :param color: color of trapezoid
    :param rotation: the angle of rotation of the figure by degrees, the angle between Ox and the bottom side of the trapezoid
    :return: None
    '''
    t.up()
    t.goto(x, y)
    # lower left corner
    p1 = t.pos()
    t.left(rotation)# Case-study #1
# Developers:  Ufilin A., Zubareva A., Berdyshev A.,
#
import turtle as t #после написания процедуры черепаха смотрит вправо!!!
import math


def isosceles_trapezoid(x, y, base1, base2, height, color, rotation):
    '''
    Function, drawing isosceles_trapezoid
    :param x: lower left corner coordinate x
    :param y: lower left corner coordinate y
    :param height: height of trapezoid
    :param base1: lower base length
    :param base2: upper base length
    :param color: color of trapezoid
    :param rotation: the angle of rotation of the figure by degrees, the angle between Ox and the bottom side of the trapezoid
    :return: None
    '''
    t.up()
    t.goto(x, y)
    # lower left corner
    p1 = t.pos()
    t.left(rotation)
    t.forward(base1)
    # lower right corner
    p2 = t.pos()
    indent = (base1 - base2) / 2
    t.backward(indent)
    t.left(90)
    t.forward(height)
    # upper right corner
    p3 = t.pos()
    t.left(90)
    t.forward(base2)
    # upper left corner
    p4 = t.pos()
    t.down()
    t.begin_fill()
    t.color("black", color)
    t.goto(p1)
    t.goto(p2)
    t.goto(p3)
    t.goto(p4)
    t.end_fill()
    t.setheading(0)

def equilateral_triangle(x, y, side, color, rotation):
    '''
    Function, drawing equilateral_triangle
    :param x: lower left corner coordinate x
    :param y: lower left corner coordinate y
    :param side: side of triangle
    :param color: color of triangle
    :param rotation: the angle of rotation of the figure by degrees, the angle between Ox and the bottom side of the triangle
    :return: None
    '''
    t.up()
    t.goto(x, y)
    t.down()
    t.left(rotation)
    t.color("black", color)
    t.begin_fill()
    for _ in range (3):
        t.forward(side)
        t.left(120)
    t.end_fill()
    t.setheading(0)

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

def crown (x, y, s, m = 'yellow', g = 'red'):
    '''
    Function, drawing crown.
    :param x: lower left point coordinate x
    :param y: lower left point coordinate y
    :param k: size of crown
    :return: None
    '''
    right_triangle(-100+x, 0+y, 50*s, 100*s, m)
    t.left(90)
    right_triangle(0+x, -50+y, 50*s, 100*s, m)
    right_triangle(100+x, -50+y, 100, 50, m)
    t.left(180)
    right_triangle(200+x, 0+y, 100*s, 50*s, m)
    rectangle(0+x, -50+y, 100*s, 50*s, 'black', m)
    t.left(90)
    right_triangle(200+x, 0+y, 65*s, 100*s, m)
    right_triangle(-100+x, 0+y, 100*s, 65*s, m)
    t.right(135)
    right_triangle(50+x, 50+y, 70*s, 70*s, m)
    rhomb(-75+x, 0+y, 32*s, 75, 'black', g, 52)
    rhomb(175+x, 0+y, 32*s, 75, 'black', g, 52)
    rhomb(50+x, 0+y, 30*s, 75, 'black', g, 52)


def main():
    '''
    Main function.
    :return: None
    '''
    t.tracer(0)
    t.right(90)
    crown(-600, 300, 1)
    t.done()

def equilateral_triangle(x, y, side, color, rotation):
    '''
    Function, drawing equilateral_triangle
    :param x: lower left corner coordinate x
    :param y: lower left corner coordinate y
    :param side: side of triangle
    :param color: color of triangle
    :param rotation: the angle of rotation of the figure by degrees, the angle between Ox and the bottom side of the triangle
    :return: None
    '''
    t.up()
    t.goto(x, y)
    t.down()
    t.left(rotation)
    t.color("black", color)
    t.begin_fill()
    for _ in range (3):
        t.forward(side)
        t.left(120)
    t.end_fill()
    t.setheading(0)

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

def crown (x, y, s, m = 'yellow', g = 'red'):
    '''
    Function, drawing crown.
    :param x: lower left point coordinate x
    :param y: lower left point coordinate y
    :param k: size of crown
    :return: None
    '''
    right_triangle(-100+x, 0+y, 50*s, 100*s, m)
    t.left(90)
    right_triangle(0+x, -50+y, 50*s, 100*s, m)
    right_triangle(100+x, -50+y, 100, 50, m)
    t.left(180)
    right_triangle(200+x, 0+y, 100*s, 50*s, m)
    rectangle(0+x, -50+y, 100*s, 50*s, 'black', m)
    t.left(90)
    right_triangle(200+x, 0+y, 65*s, 100*s, m)
    right_triangle(-100+x, 0+y, 100*s, 65*s, m)
    t.right(135)
    right_triangle(50+x, 50+y, 70*s, 70*s, m)
    rhomb(-75+x, 0+y, 32*s, 75, 'black', g, 52)
    rhomb(175+x, 0+y, 32*s, 75, 'black', g, 52)
    rhomb(50+x, 0+y, 30*s, 75, 'black', g, 52)

def rabbit(x, y):
    '''
    Function, drawing rabbit.
    :param x: coordinate x of rabbit's head
    :param y: coordinate y of rabbit's head
    :return: None
    '''
    # rabbit's head
    circle(x, y, 40, "orange")
    # rabbit's left ear
    equilateral_triangle(x - 10, y + 80, 70, "orange", 90)
    # rabbit's right ear
    equilateral_triangle(x + 10, y + 80, 70, "orange", 30)
    # rabbit's body
    equilateral_triangle(x - 100, y - 175, 200, "pink", 0)
    # rabbit's left leg
    isosceles_trapezoid(x - 70, y - 195, 60, 30, 20, "orange", 0)
    # rabbit's right leg
    isosceles_trapezoid(x + 15, y - 195, 60, 30, 20, "orange", 0)
    # rabbit's left arm
    circle(x - 55, y - 80, 20, "orange")
    # rabbit's right arm
    circle(x + 55, y - 80, 20, "orange")


def main():
    '''
    Main function.
    :return: None
    '''
    t.tracer(0)
    t.hideturtle()
    t.right(90)
    crown(-600, 300, 1)
    rabbit(-550, 50)
    t.update()
    t.done()


main()
