from tkinter import *
from PIL import ImageTk, Image
import requests

codigo=""

def key_pressed(event):
    global codigo
    if event.keysym == "Return":
        print(codigo)
        URL = "http://localhost/api/index2.php?codigo=" + codigo
        Respuesta = requests.get(URL)
        #print(Respuesta.json())

        Datos = Respuesta.json()
        print(Datos["Status"])
        
        codigo=""
        if Datos["Status"] == 200:
            loadImg("./Img/Productos/" + Datos["Imagen"])
            labelProducto.config(text="Nombre del Producto: " + Datos["Nombre"])
            labelPrecio.config(text="Precio del Producto: " + Datos ["Precio"])
            print(Datos["Nombre"])
            print(Datos["Precio"])
            print(Datos["Imagen"])
        else:
            loadImg("./Img/error.png")
            labelProducto.config(text="Nombre del Producto no existe")
            labelPrecio.config(text="Precio del Producto no existe")
    else:
        codigo+=event.keysym

def loadImg(imgPath):
    render = ImageTk.PhotoImage(Image.open(imgPath))
    img = Label(Ventana, image=render, width=600, height=600)
    img.image = render
    img.place(relx=0.5, rely=0.5, anchor='center')
    #productos = readjson()

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
labelTitulo.place(x = Vwidth / 3.5 - labelTitulo.winfo_width() / 3.5, y = 50)

#Labels 2
labelProducto = Label(Ventana, text = "Producto: " + str(Vwidth), font = Subtitulos)
labelProducto.pack()
labelProducto.place(x = 15, y = 100)

#Labels 3
labelPrecio = Label(Ventana, text = "Precio: " + str(Vheight), font = Subtitulos)
labelPrecio.pack()
labelPrecio.place(x = 15, y = 150)

#El Main Loop Va Ha Lo Último
Ventana.bind('<Key>', key_pressed)
Ventana.mainloop()