import tkinter as tk
import turtle as tt

def dibujar_rectangulo():
    x1 = 0
    y1 = 0
    x2 = 400
    y2 = -400
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

def dibujar_cuadrado():
    x1 = 0
    y1 = 0
    x2 = 400
    y2 = -400
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
    for i in range(400):
        tt.goto(x,y)
        if i<=99:
            x=x+incrementoX
            y=y
        elif i<=199:
            x=x
            y=y+incrementoY
        elif i<=299:
            x=x-incrementoX
            y=y
        elif i<=399:
            x=x
            y=y-incrementoY

def dibujar_cuadrado_floodfill():
    x1 = 0
    y1 = 0
    x2 = 200
    y2 = 200
    canvas = [[0 for i in range(200)] for j in range(200)]
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
    for i in range(200):
        tt.color("black")
        tt.goto(x,y)
        canvas[x][y]="black"
        if i<50:
            x=round(x+incrementoX)
            y=y
        elif i<100:
            x=x
            y=round(y+incrementoY)
        elif i<150:
            x=round(x-incrementoX)
            y=y
        elif i<200:
            x=x
            y=round(y-incrementoY)
    floodfill4(x1, y1, "black", "blue", canvas)
    colorear(canvas)

def floodfill4(x, y, old_color, new_color, canvas):
    if x < 0 or x >= 200 or y < 0 or y >= 200 or canvas[x][y] != old_color:
        return
    else:
        canvas[x][y] = new_color
        floodfill4(x, y+1, old_color, new_color, canvas)
        floodfill4(x, y-1, old_color, new_color, canvas)
        floodfill4(x+1, y, old_color, new_color, canvas)
        floodfill4(x-1, y, old_color, new_color, canvas)

def colorear(canvas):
    tt.hideturtle()
    for x in range(50):
        for y in range(50):
            if canvas[x][y] == "black":
                tt.color("black")
            elif canvas[x][y] == "blue":
                tt.color("blue")
            tt.goto(x,y)

def escalado_cuadrado():
    x1 = 0
    y1 = 0
    x2 = 400*2
    y2 = -400*2
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

    for i in range(800):
        tt.goto(x,y)
        if i<200:
            x=x+incrementoX
            y=y
        elif i<400:
            x=x
            y=y+incrementoY
        elif i<600:
            x=x-incrementoX
            y=y
        elif i<800:
            x=x
            y=y-incrementoY

def limpiar_lienzo():
    tt.clear()

def minimizar():
    ventana.iconify()

def maximizar():
    if ventana.state() == 'zoomed':
        ventana.state('normal')
    else:
        ventana.state('zoomed')

def cambia_color(event, boton):
    if boton==boton_minimizar or boton==boton_maximizar:
        boton.configure(background="#AA336A")
    else:
        boton.configure(background="#c00000")

def restaura_color(event, boton):
    if boton==boton_minimizar or boton==boton_maximizar:
        boton.configure(background="pink")
    else:
        boton.configure(background="pink")


# Creamos la ventana principal
ventana = tk.Tk()
ventana.geometry("600x800")
# ventana.overrideredirect(True)
ventana.configure(border=0)
ventana.config(bg="pink")
ventana.title("Proyecto 1- Claudia & Luis 1SF141")

# Configuramos la estructura de cuadrícula
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=0)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=0)
ventana.rowconfigure(3, weight=0)

frame_fila0 = tk.Frame(ventana, bg="#AA336A")
frame_fila0.grid(row=0, column=0, columnspan=4, sticky="nsew")

# botones de la ventana
boton_rectangulo = tk.Button(ventana, text="Rectángulo", command=dibujar_rectangulo)
boton_cuadrado = tk.Button(ventana, text="Cuadrado", command=dibujar_cuadrado)
boton_circulo = tk.Button(ventana, text="Rellenar", command=dibujar_cuadrado_floodfill)
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lienzo)
boton_animacion = tk.Button(ventana, text="Escalado", command=escalado_cuadrado)

# Posicionamos los botones en la cuadrícula
boton_rectangulo.grid(row=2, column=0, padx=10, pady=10)
boton_cuadrado.grid(row=2, column=1, padx=10, pady=10)
boton_circulo.grid(row=2, column=2, padx=10, pady=10)
boton_limpiar.grid(row=3, column=0, padx=10, pady=10)
boton_animacion.grid(row=3, column=1, padx=10, pady=10)

# Botones personalizados
boton_minimizar = tk.Button(ventana, text='-', command=minimizar, foreground="white", background="pink", height=2, width=4)
boton_minimizar.configure(highlightthickness=0, bd=0)
boton_minimizar.bind("<Enter>", lambda event: cambia_color(event, boton_minimizar))
boton_minimizar.bind("<Leave>", lambda event: restaura_color(event, boton_minimizar))
boton_minimizar.grid(row=0, column=2, sticky="NE", padx=0, pady=0)

boton_maximizar = tk.Button(ventana, text='[]', command=maximizar, foreground="white", background="pink", height=2, width=4)
boton_maximizar.configure(highlightthickness=0, bd=0)
boton_maximizar.bind("<Enter>", lambda event: cambia_color(event, boton_maximizar))
boton_maximizar.bind("<Leave>", lambda event: restaura_color(event, boton_maximizar))
boton_maximizar.grid(row=0, column=3, sticky="NE", padx=0, pady=0)

boton_salir = tk.Button(ventana, text="X", command=ventana.quit, foreground="white", background="pink", height=2, width=4)
boton_salir.configure(highlightthickness=0, bd=0)
boton_salir.bind("<Enter>", lambda event: cambia_color(event, boton_salir))
boton_salir.bind("<Leave>", lambda event: restaura_color(event, boton_salir))
boton_salir.grid(row=0, column=4, sticky="NE", padx=0, pady=0)

# Creamos una zona de dibujo para turtle
lienzo = tk.Canvas(ventana)
lienzo.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="NSEW")

# Inicializamos turtle
tt = tt.RawTurtle(lienzo)
tt.speed(0)

# Para que la ventana se mantenga abierta
ventana.mainloop()
