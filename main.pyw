from ast import If
from cProfile import label
from sqlite3 import Row
from tkinter import *
import tkinter as tk
import time
import os
from tkinter import font
from isort import file
from matplotlib.pyplot import text
from sqlalchemy import column
from tables import ComplexAtom

ancho_root = 350
alto_root = 150

#root
root = Tk()
root.title("ViolencioVirus")
root.geometry("350x150")
root.resizable(0, 0)
root.config(bg="gray")

root.iconphoto(True, PhotoImage(file='img/virus.png'))

#posicionamiento de root
x_root = root.winfo_screenwidth() // 2 - ancho_root // 2
y_root = root.winfo_screenheight() // 2 - alto_root // 2

posicion = str(ancho_root) + "x" + str(alto_root) + "+" + str(x_root) + "+" + str(y_root)
root.geometry(posicion)

#texto 
Principal = Label(root, bg="gray").pack()
Texto1 = Label(root, bg="gray", text="Si quieres ejecutarlo pulsa <Si> y si no,").pack()
Texto1 = Label(root, bg="gray", text=" simplemente pulsa <No> y nada pasará").pack()

#funciones
def SI():

    ancho_ventana = 500
    alto_ventana = 200

    #ventana
    ventana = Tk()
    ventana.title("ViolencioVirus")
    ventana.geometry("500x200")
    ventana.config(bg="gray")
    ventana.resizable(0, 0)

    #posicionamiento de ventana
    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    ventana.geometry(posicion)

    root.destroy()

    happy = "😃"
    angry = "😠"
    superAngry = "😡"

    #texto
    Text1 = Label(ventana, bg="gray", text="Estoy de mal humor, ¿Qué debo hacer?")
    Text1.place(x=110, y=40)
    Text2 = Label(ventana, bg="gray", text=angry)
    Text2.configure(font=(20))
    Text2.place(x=225, y=60)

    
    #Input
    queHacer = Entry(ventana, text="Que hacer")
    queHacer.place(x=155, y=80)

    #función de probar
    def Probar():
        if (queHacer.get() == "1"):
            Text2.configure(text=happy)
            ventana.config(bg="green")
            time.sleep(0.01)
            Text1.config(bg="green")
            time.sleep(0.01)
            Text2.config(bg="green")
        elif (queHacer.get() == "2"):
            Text2.configure(text=happy)
            ventana.config(bg="green")
            time.sleep(0.01)
            Text1.config(bg="green")
            time.sleep(0.01)
            Text2.config(bg="green")
        elif (queHacer.get() == "3"):
            Text2.configure(text=happy)
            ventana.config(bg="green")
            time.sleep(0.01)
            Text1.config(bg="green")
            time.sleep(0.01)
            Text2.config(bg="green")
        elif (queHacer.get() == "5"):
            Text2.configure(text=happy)
            ventana.config(bg="green")
            time.sleep(0.01)
            Text1.config(bg="green")
            time.sleep(0.01)
            Text2.config(bg="green")
        elif (queHacer.get() == "7"):
            Text2.configure(text=happy)
            ventana.config(bg="green")
            time.sleep(0.01)
            Text1.config(bg="green")
            time.sleep(0.01)
            Text2.config(bg="green")
        elif (queHacer.get() == "9"):
            Text2.configure(text=happy)
            ventana.config(bg="green")
            time.sleep(0.01)
            Text1.config(bg="green")
            time.sleep(0.01)
            Text2.config(bg="green")
        else:
            Text2.configure(text=superAngry)
            Text1.config(bg="red")
            time.sleep(0.01)
            Text2.config(bg="red")
            time.sleep(0.01)
            ventana.config(bg="red")

    #función de opciones
    def Opciones():
        
        opciones = Tk()
        opciones.title("Opciones")
        opciones.geometry("500x700")
        opciones.config(bg="gray")
        opciones.resizable(0, 0)

        #function de matar todo
        def matarTodoF():
            ventana.destroy()
            opciones.destroy()

        #matar todo
        matarTodo = Button(opciones, command=matarTodoF, bg="red", text="X")
        matarTodo.place(x=465, y=0)

        #opciones texto
        texto1 = Label(opciones, bg="gray", text="1-Salir a pasear").pack()
        texto1 = Label(opciones, bg="gray", text="2-Jugar con tu mascota").pack()
        texto1 = Label(opciones, bg="gray", text="3-Salir al campo").pack()
        texto1 = Label(opciones, bg="gray", text="4-Tratar mal a las personas").pack()
        texto1 = Label(opciones, bg="gray", text="5-Estar con tu familia").pack()
        texto1 = Label(opciones, bg="gray", text="6-Insultar al aire").pack()
        texto1 = Label(opciones, bg="gray", text="7-Estar con tus amigos").pack()
        texto1 = Label(opciones, bg="gray", text="8-Pensar en lo que no te gusta").pack()
        texto1 = Label(opciones, bg="gray", text="9-Estar con personas que te caen bien").pack()
        texto1 = Label(opciones, bg="gray", text="10-Tratar con agresividad a las cosas que te rodean").pack()
        texto1 = Label(opciones, bg="gray", text="11-Repartir puñetazos por la calle").pack()

    def Sintomas():

        sintomas = Tk()
        sintomas.title("Síntomas")
        sintomas.geometry("500x700")
        sintomas.resizable(0, 0)
        sintomas.config(bg="gray")

        #function de matar todo
        def matarTodoF():
            sintomas.destroy()

        #matar todo
        matarTodo = Button(sintomas, command=matarTodoF, bg="red", text="X")
        matarTodo.place(x=465, y=0)

        #texto síntomas
        sintomasTexto = Label(sintomas, bg="gray", text="Te vuelve agresivo").pack()
        sintomasTexto = Label(sintomas, bg="gray", text="Te marea").pack()
        sintomasTexto = Label(sintomas, bg="gray", text="Bulling").pack()
        sintomasTexto = Label(sintomas, bg="gray", text="Impaciencia").pack()
        sintomasTexto = Label(sintomas, bg="gray", text="Prepotencia").pack()
        sintomasTexto = Label(sintomas, bg="gray", text="Adicción al móvil").pack()
        sintomasTexto = Label(sintomas, bg="gray", text="Mentir compulsivamente").pack()
        sintomasTexto = Label(sintomas, bg="gray", text="Violaciones").pack()
        sintomasTexto = Label(sintomas, bg="gray", text="Sobreexigirse").pack()
        sintomasTexto = Label(sintomas, bg="gray", text="Pesimismo").pack()
        sintomasTexto = Label(sintomas, bg="gray", text="Inmadurez").pack()
        sintomasTexto = Label(sintomas, bg="gray", text="Envidia").pack()
        sintomasTexto = Label(sintomas, bg="gray", text="Vengativo").pack()
        sintomasTexto = Label(sintomas, bg="gray", text="Pereza").pack()
        sintomasTexto = Label(sintomas, bg="gray", text="Racismo").pack()
        sintomasTexto = Label(sintomas, bg="gray", text="Sexismo").pack()
        sintomasTexto = Label(sintomas, bg="gray", text="Superficialidad").pack()
        sintomasTexto = Label(sintomas, bg="gray", text="Pereza").pack()
        sintomasTexto = Label(sintomas, bg="gray", text="*Adicción al móvil*").pack()

        sintomas.mainloop()
    #botón
    queHacerBTN = Button(ventana, command=Probar, text="Probar")
    queHacerBTN.place(x=200, y=120)
    Opciones = Button(ventana, command=Opciones, text="Opciones")
    Opciones.place(x=150, y=160)  
    Sintomas = Button(ventana, command=Sintomas, text="Síntomas")
    Sintomas.place(x=240, y=160)


    ventana.mainloop()

def noEjecutar():
    time.sleep(0.01)
    root.destroy()
#botones
ejecutar = Button(root, bg="white", command=SI, text="Si").place(x=100, y=100)
NoEjecutar = Button(root, bg="white", command=noEjecutar, text="No").place(x=200, y=100)


root.mainloop()
