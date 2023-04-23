from ctypes import *
from re import X
import tkinter as tk
from turtle import width
from PIL import ImageTk, Image
from matplotlib import image
import turtle

#PROGRAMACIÓN

#CLASES
def close_window():
    window.destroy()


def draw_rectangle():
    t=turtle.Turtle()
    
    turtle.color('blue', 'black')
    turtle.begin_fill()

    draw = turtle.RawTurtle(canvas)
    
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



def draw_square():
    canvas.create_rectangle(0, 0, 150, 150, fill = "#f95738", outline = "#f95738")

def rotate():
    canvas.create_rectangle(0, 0, 150, 150, fill = "#f95738", outline = "#f95738")

def fulfill():
    canvas.create_polygon(0, 0, 150, 0, 75, 150, fill = "#f95738", outline = "#f95738")

#INTERFAZ GUI

#declarar ventana
window = tk.Tk()
window.geometry("500x600")
window.title("Proyecto 1- Claudia & Luis 1SF141")
window.config(bg='#ee964b')

#labels
label1 = tk.Label(window, text = "PROYECTO 1", bg ='#ee964b', font= ("Consolas", 24))
label1.place(x = 155, y= 50)

label2 = tk.Label(window, text = "CLAUDIA HERNÁNDEZ Y LUIS MARQUEZ", bg ='#ee964b', font= ("Consolas", 13))
label2.place(x = 90, y= 20)

#canvas
canvas = tk.Canvas(window, bg ="#faf0ca", height = 250, width = 300)
canvas.place(x = 90, y = 100)


#buttons
button1 = tk.Button(window, bg='#f4d35e', text = "X", width=  3, height=  1, command= close_window)
button2 = tk.Button(window, bg='#f95738', text = "TRIÁNGULO", width=  15, height=  3, command= draw_rectangle())
button3 = tk.Button(window, bg='#f95738', text = "CUADRADO", width=  15, height=  3, command= draw_square)
button4 = tk.Button(window, bg='#0d3b66', fg= '#faf0ca' ,text = "RELLENAR", width=  15, height=  3)
button5 = tk.Button(window, bg='#0d3b66',  fg= '#faf0ca', text = "ROTAR", width=  15, height=  3)
button6 = tk.Button(window, bg='#f4d35e', text = "REPETIR", width=  42, height=  2)

button1.place(x = 470, y = 0) #x
button2.place(x = 90, y = 370) #triangulo
button3.place(x = 278, y = 370) #rectangulo
button4.place(x = 90, y = 450) #rellenar figura
button5.place(x = 278, y = 450) #lo otro que pide
button6.place(x = 90, y = 525) #repetir

window.mainloop()

""""
if (button2 == True):
    draw_triangle()
elif (button3 == True):
    draw_rectangle() """ #esto no funciona AÚN




