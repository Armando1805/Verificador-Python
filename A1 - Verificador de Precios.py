from tkinter import *
from PIL import ImageTk, Image
import json

codigo=""

def readjson():
    with open("Json/Productos.json") as json_file:
        return json.load(json_file).get("productos")

def key_pressed(event):
    global codigo
    if event.keysym == "Return":
        print(codigo)
        item = productos.setdefault(codigo, ["None", "0.00", "./Img/Error.gif"])
        codigo=""
        if item is not None:
            loadImg(item[-1])
            labelProducto.config(text=item[0])
            labelPrecio.config(text=item[1])
        else:
            loadImg("ex.gif")
    else:
        codigo+=event.keysym

def loadImg(imgPath):
    render = ImageTk.PhotoImage(Image.open(imgPath))
    img = Label(Ventana, image=render, width=500, height=500)
    img.image = render
    img.place(x=Vwidth/2 - 250, y=250)
productos = readjson()

#Ventanas
Ventana = Tk()
Ventana.geometry("1000x800")
Ventana.title("Verificador de Precios")
Ventana.update()

#Letras
Titulos = ("Arial", 25, "bold")
Subtitulos = ("Arial", 20, "bold")

#Caracteristicas
Vwidth = Ventana.winfo_width()
Vheight = Ventana.winfo_height()
loadImg("Img/Lector.gif")

#Labels 1
labelTitulo = Label(Ventana, text = "Verificador de Productos", font = Titulos)
labelTitulo.pack()
labelTitulo.place(x = Vwidth / 3.5 - labelTitulo.winfo_width() / 3.5, y = 105)

#Labels 2
labelProducto = Label(Ventana, text = "Producto: " + str(Vwidth), font = Subtitulos)
labelProducto.pack()
labelProducto.place(x = 15, y = 250)

#Labels 3
labelPrecio = Label(Ventana, text = "Precio: " + str(Vheight), font = Subtitulos)
labelPrecio.pack()
labelPrecio.place(x = 15, y = 300)

#El Main Loop Va Ha Lo Último
Ventana.bind('<Key>', key_pressed)
Ventana.mainloop()