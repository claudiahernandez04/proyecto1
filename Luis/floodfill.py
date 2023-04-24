import turtle as tt

def dibujar_cuadrado(x1,x2,y1,y2,canvas):
    dx = x2 - x1
    dy = y2 - y1
    pasos=0
    incrementoX=0
    incrementoY=0
    if(abs(dx)>abs(dy)):
        pasos=abs(dx)
    else:
        pasos=abs(dy)  
    incrementoX = dx / pasos
    incrementoY = dy / pasos
    x=x1
    y=y1
    for i in range(100):
        tt.color("black")
        tt.goto(x,y)
        canvas[x][y]="black"
        if i<25:
            x=round(x+incrementoX)
            y=y
        elif i<50:
            x=x
            y=round(y+incrementoY)
        elif i<75:
            x=round(x-incrementoX)
            y=y
        elif i<100:
            x=x
            y=round(y-incrementoY)
    floodfill(x1, y1, "black", "blue", canvas)
    colorear(canvas)

def floodfill(x, y, old_color, new_color, canvas):
    if x < 0 or x >= 100 or y < 0 or y >= 100 or canvas[x][y] != old_color:
        return
    else:
        canvas[x][y] = new_color
        floodfill(x, y+1, old_color, new_color, canvas)
        floodfill(x, y-1, old_color, new_color, canvas)
        floodfill(x+1, y, old_color, new_color, canvas)
        floodfill(x-1, y, old_color, new_color, canvas)
        
def colorear(canvas):
    tt.hideturtle()
    for x in range(25):
        for y in range(25):
            if canvas[x][y] == "black":
                tt.color("black")
            elif canvas[x][y] == "blue":
                tt.color("blue")
            tt.goto(x,y)

x1 = 0
y1 = 0
x2 = 100
y2 = 100
lienzo = [[0 for i in range(100)] for j in range(100)]
dibujar_cuadrado(x1,x2,y1,y2,lienzo)
tt.mainloop()
