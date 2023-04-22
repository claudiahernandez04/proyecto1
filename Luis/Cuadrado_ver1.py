import turtle

t=turtle.Turtle()

turtle.color('blue', 'black')
turtle.begin_fill()

x1 = 1
y1 = 1
x2 = 500
y2 = 500
dx = x2 - x1
dy = y2 - y1
pasos=0
incrementoX=0
incrementoY=0

if(abs(dx)>abs(dy)):
    pasos=abs(dx)
else:
    pasos=abs(dy)  
incrementoX=dx/pasos
incrementoY=dy/pasos

x=x1
y=y1

for i in range(300):
    t.goto(x,y)
    if i<=99:
        x=x+incrementoX
        y=y
    elif i<=149:
        x=x
        y=y+incrementoY
    elif i<=249:
        x=x-incrementoX
        y=y
    elif i<=299:
        x=x
        y=y-incrementoY

turtle.end_fill()
turtle.hideturtle()
turtle.mainloop()
