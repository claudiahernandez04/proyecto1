import turtle

def bresenham_circle(center, radius):
    x0, y0 = center
    x = radius
    y = 0
    err = 0

    while x >= y:
        turtle.speed(0)
        turtle.goto(x + x0, y + y0)
        turtle.goto(y + x0, x + y0)
        turtle.goto(-x + x0, y + y0)
        turtle.goto(-y + x0, x + y0)
        turtle.goto(-x + x0, -y + y0)
        turtle.goto(-y + x0, -x + y0)
        turtle.goto(x + x0, -y + y0)
        turtle.goto(y + x0, -x + y0)
        y += 1
        err += 1 + 2*y
        if 2*(err - x) + 1 > 0:
            x -= 1
            err += 1 - 2*x

turtle.penup()
center = (0, 0)
radius = 100
turtle.goto(center)
turtle.pendown()
bresenham_circle(center, radius)
turtle.done()
