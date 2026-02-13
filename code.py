# Case-study #1
# Developers:  Ufilin A., Zubareva A., Berdyshev A.,
#
import turtle as t #после написания процедуры черепаха смотрит вправо!!!
import math


# def isosceles_trapezoid(x, y, base1, base2, height, color, rotation):
#     '''
#     Function, drawing isosceles_trapezoid
#     :param x: lower left corner coordinate x
#     :param y: lower left corner coordinate y
#     :param height: height of trapezoid
#     :param base1: lower base length
#     :param base2: upper base length
#     :param color: color of trapezoid
#     :param rotation: the angle of rotation of the figure by degrees, the angle between Ox and the bottom side of the trapezoid
#     :return: None
#     '''
#     t.up()
#     t.goto(x, y)
#     # lower left corner
#     p1 = t.pos()
#     t.left(rotation)# Case-study #1



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

def rectangle(x, y, sidea, sideb, color = "white", rotation = 0):
    '''
    Function, drawing rectangle
    :param x: lower left corner coordinate x
    :param y: lower left corner coordinate y
    :param sidea: lower and upper side of rectangle (in case rotation equals to 0)
    :param sideb: left and right side of rectangle (in case rotation equals to 0)
    :param color: color of rectangle
    :param rotation: the angle of rotation of the figure by degrees, the angle between Ox and the bottom side of the rectangle
    :return: None
    '''
    t.up()
    t.goto(x, y)
    t.down()
    t.left(rotation)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(sidea)
        t.left(90)
        t.forward(sideb)
        t.left(90)
    t.end_fill()
    t.setheading(0)
    t.color("black")

def rhomb(x, y, side, angle, color = "white", rotation = 0):
    '''
    Function, drawing rhomb
    :param x: lower left corner coordinate x
    :param y: lower left corner coordinate y
    :param side: side of rhomb
    :param color: color of rhomb
    :param rotation: the angle of rotation of the figure by degrees, the angle between Ox and the bottom side of the rhomb
    :return: None
    '''
    t.up()
    t.goto(x, y)
    t.down()
    t.left(rotation)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(side)
        t.left(angle)
        t.forward(side)
        t.left(180 - angle)
    t.end_fill()
    t.setheading(0)
    t.color("black")

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

def right_triangle (x, y, a, b, color, rotation = 0):
    '''
    Function, drawing right_triangle.
    :param x: point between legs coordinate x
    :param y: point between legs coordinate y
    :param a: first leg lenght
    :param b: second leg lenght
    :param color: color of triangle
    :param rotation: rotation of triangle, angle between Ox and the lowest side in case rotation equals to 0
    :return: None
    '''
    t.up()
    t.setposition(x, y)
    t.down()
    t.color('black', color)
    t.begin_fill()
    t.left(rotation)
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

def crown (x, y, m = 'yellow', g = 'red'):
    '''
    Function, drawing crown.
    :param x: lower left point coordinate x
    :param y: lower left point coordinate y
    :param k: size of crown
    :return: None
    '''
    right_triangle(-100+x, 0+y, 50, 100, m)
    t.left(90)
    right_triangle(0+x, -50+y, 50, 100, m)
    right_triangle(100+x, -50+y, 100, 50, m)
    t.left(180)
    right_triangle(200+x, 0+y, 100, 50, m)
    rectangle(0+x, -50+y, 100, 50, m)
    t.left(90)
    right_triangle(200+x, 0+y, 65, 100, m)
    right_triangle(-100+x, 0+y, 100, 65, m)
    t.right(135)
    right_triangle(50+x, 50+y, 70, 70, m)
    rhomb(-75+x, 0+y, 32, 75, g, 52)
    rhomb(175+x, 0+y, 32, 75, g, 52)
    rhomb(50+x, 0+y, 30, 75, g, 52)

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

def square(x, y, s=1):
    '''
    Function, drawing square.
    :param x: coordinate x of right upper point
    :param y: coordinate y of right upper point
    :param s: scale
    :return: None
    '''
    # orange left center side triangle
    right_triangle(x, y, 100*s, 100*s, "orange", rotation=135)
    # pink upper side triangle
    right_triangle(x, y, 100*s, 100*s, "pink", rotation=45)
    # rectangle
    rectangle(x, y, 50*s, 50*s, "orange", rotation=-45)
    # yellow upper right triangle (between rectangle and upper side triangle)
    right_triangle(x + 100*s*0.5/2**0.5, y + 100*s*0.5/2**0.5, 50 * s, 50 * s, "yellow", rotation=-45)
    # red lower right corner triangle
    right_triangle(x + 100*s/2**0.5, y - 100*s/2**0.5, (100 * s)/2**0.5, (100 * s)/2**0.5, "red", rotation=90)
    # pink center triangle (between rectangle and orange left side triangle)
    right_triangle(x, y, 50 * s, 50 * s, "pink", rotation=-135)
    # green bottom side triangle 1
    right_triangle(x, y - 100*s/2**0.5, 50 * s, 50 * s, "green", rotation=45)
    # green bottom side triangle 2
    right_triangle(x - 100*s*0.5/2**0.5, y - 100*s*0.5/2**0.5, 50 * s, 50 * s, "green", rotation=-135)

def sword(x, y, s):
    '''
    Function, drawing sword.
    :param x: lower point coordinate x
    :param y: lower point coordinate y
    :param k: size of sword
    :return: None
    '''
    rectangle(0 + x, 0 + y, 30, 60, 'black', 'gray', 90)
    rhomb(15 + x, (-math.sqrt(1800)) / 2 + y, 30, 90, 'black', 'black', 45)
    right_triangle(15 + x, 90 + y)



def main():
    '''
    Main function.
    :return: None
    '''
    t.tracer(0)
    t.hideturtle()
    t.right(90)
    crown(-600, 300)
    rabbit(-550, 50)
    square(-200, 250, 1.5)
    t.update()
    t.done()


main()
