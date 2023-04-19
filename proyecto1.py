from ctypes import *
from re import X
import tkinter as tk
from turtle import width
from PIL import ImageTk, Image
from matplotlib import image



#declarar ventana
window = tk.Tk()
window.geometry("500x600")
window.title("Proyecto 1")
window.config(bg='#DFFC9D')

#labels
label1 = tk.Label(window, text = "Proyecto 1", bg ='#DFFC9D', font= (44))
label1.place(x = 195, y= 50)




#buttons
button1 = tk.Button(window, bg='light yellow', text = "X", width=  3, height=  1)
button2 = tk.Button(window, bg='light yellow', text = "Opción1", width=  30, height=  10)
button3 = tk.Button(window, bg='light yellow', text = "Opción2", width=  30, height=  10)
button4 = tk.Button(window, bg='light yellow', text = "Repetir", width=  6, height=  2)

button1.place(x = 470, y = 0)
button2.place(x = 20, y = 200)
button3.place(x = 250, y = 200)
button4.place(x = 225, y = 400)


#img = ImageTk.PhotoImage(Image.open("purple.jpg"), Image.ANTIALIAS)

#label = tk.Label(window, image = img, width= 100, height =135)
#label.place(x=30, y=37)

window.mainloop()
