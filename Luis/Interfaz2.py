import tkinter as tk
import turtle as tt
from tkinter import ttk

def dibujar_rectangulo():
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
        tt.goto(x,y)
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

    
    # tt.penup()
    # tt.goto(-50, 50)
    # tt.pendown()
    # tt.setheading(0)
    # tt.forward(100)
    # tt.right(90)
    # tt.forward(50)
    # tt.right(90)
    # tt.forward(100)
    # tt.right(90)
    # tt.forward(50)

def dibujar_cuadrado():
    tt.penup()
    tt.goto(-50, 50)
    tt.pendown()
    tt.setheading(0)
    tt.forward(100)
    tt.right(90)
    tt.forward(100)
    tt.right(90)
    tt.forward(100)
    tt.right(90)
    tt.forward(100)

def limpiar_lienzo():
    tt.clear()

def animar_turtle():
    tt.penup()
    tt.goto(-100, -100)
    tt.pendown()
    tt.speed(1)
    for i in range(4):
        tt.forward(200)
        tt.right(90)

def minimizar():
    ventana.iconify()

def maximizar():
    if ventana.state() == 'zoomed':
        ventana.state('normal')
    else:
        ventana.state('zoomed')

ventana = tk.Tk()
ventana.overrideredirect(True)

# Configuramos la estructura de cuadrícula
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=0)

# Creamos los botones
boton_rectangulo = tk.Button(ventana, text="Rectángulo", command=dibujar_rectangulo)
boton_cuadrado = tk.Button(ventana, text="Cuadrado", command=dibujar_cuadrado)
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lienzo)
boton_animacion = tk.Button(ventana, text="Animación", command=animar_turtle)

# Posicionamos los botones en la cuadrícula
boton_rectangulo.grid(row=2, column=0, padx=10, pady=10)
boton_cuadrado.grid(row=2, column=1, padx=10, pady=10)
boton_limpiar.grid(row=2, column=2, padx=10, pady=10)
boton_animacion.grid(row=2, column=3, padx=10, pady=10)

# Agregamos el botón para cerrar la ventana
# style = ttk.Style()
# boton_minimizar = ttk.Button(ventana, text='-', command=minimizar, style='Titlebar.TButton')
# boton_minimizar.grid(row=0, column=0, padx=2, pady=2)
# boton_maximizar = ttk.Button(ventana, text='[]', command=maximizar, style='Titlebar.TButton')
# boton_maximizar.grid(row=0, column=1, padx=2, pady=2)
# boton_cerrar = ttk.Button(ventana, text='x', command=ventana.quit, style='Titlebar.TButton')
# boton_cerrar.grid(row=0, column=2, padx=2, pady=2)


boton_minimizar = tk.Button(ventana, text='-', command=minimizar)
boton_minimizar.grid(row=0, column=2, sticky="NE", padx=10, pady=10)
boton_maximizar = tk.Button(ventana, text='[]', command=maximizar)
boton_maximizar.grid(row=0, column=3, sticky="NE", padx=10, pady=10)
boton_salir = tk.Button(ventana, text="X", command=ventana.quit)
boton_salir.grid(row=0, column=4, sticky="NE", padx=10, pady=10)

# Creamos una zona de dibujo para turtle
lienzo = tk.Canvas(ventana)
lienzo.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="NSEW")

# Inicializamos turtle
tt = tt.RawTurtle(lienzo)
tt.speed(0)

# Iniciamos el loop de la aplicación
ventana.mainloop()
