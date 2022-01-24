from ast import If
from cProfile import label
from tkinter.ttk import *
from sqlite3 import Row
from tkinter import *
import tkinter as tk
from tkinter import font
import webbrowser
import time
import os

ancho_root = 350
alto_root = 150

#root
root = Tk()
root.title("ViolencioVirus")
root.geometry("500x150")
root.resizable(0, 0)
root.config(bg="gray")

root.iconphoto(True, PhotoImage(file='img/virus.png'))

#posicionamiento de root
x_root = root.winfo_screenwidth() // 2 - ancho_root // 2
y_root = root.winfo_screenheight() // 2 - alto_root // 2

posicion = str(ancho_root) + "x" + str(alto_root) + "+" + str(x_root) + "+" + str(y_root)
root.geometry(posicion)

#texto 
Principal = Label(root, bg="gray").place()
Texto1M = Label(root, bg="gray", text="Si quieres ejecutarlo pulsa <Si> y si no,").place(x=35, y=40)
Texto2M = Label(root, bg="gray", text=" simplemente pulsa <No> y nada pasará").place(x=35, y=75)

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
    Text1 = Label(ventana, bg="gray", text="Estoy enfadado, ¿Qué puedo hacer para que se me pase?")
    Text1.place(x=60, y=40)
    Text2 = Label(ventana, bg="gray", text=angry)
    Text2.configure(font=(20))
    Text2.place(x=225, y=60)

    
    #Input
    queHacer = Entry(ventana, text="Que hacer")
    queHacer.place(x=155, y=80)

    #función de probar
    def Probar():

        if (queHacer.get() == "1"):
            f = open("datos.txt","w")
            f.write("Hola, soy HackerCloud")
            f.close()
            Text2.configure(text=happy)
            ventana.config(bg="green")
            time.sleep(0.01)
            Text1.config(bg="green")
            time.sleep(0.01)
            Text2.config(bg="green")
        elif (queHacer.get() == "0"):
            f = open("datos.txt","w")
            f.write("Hola, soy HackerCloud")
            f.close()
            time.sleep(0.01)
            Text2.configure(text=angry)    
            time.sleep(0.01)
            ventana.config(bg="gray")        
            time.sleep(0.01)
            Text1.configure(bg="gray")
            time.sleep(0.01)
            Text2.configure(bg="gray")
        elif (queHacer.get() == "2"):
            f = open("datos.txt","w")
            f.write("Hola, soy HackerCloud")
            f.close()
            Text2.configure(text=happy)
            ventana.config(bg="green")
            time.sleep(0.01)
            Text1.config(bg="green")
            time.sleep(0.01)
            Text2.config(bg="green")
        elif (queHacer.get() == "3"):
            f = open("datos.txt","w")
            f.write("Hola, soy HackerCloud")
            f.close()            
            Text2.configure(text=happy)
            ventana.config(bg="green")
            time.sleep(0.01)
            Text1.config(bg="green")
            time.sleep(0.01)
            Text2.config(bg="green")
        elif (queHacer.get() == "5"):
            f = open("datos.txt","w")
            f.write("Hola, soy HackerCloud")
            f.close()            
            Text2.configure(text=happy)
            ventana.config(bg="green")
            time.sleep(0.01)
            Text1.config(bg="green")
            time.sleep(0.01)
            Text2.config(bg="green")
        elif (queHacer.get() == "7"):
            f = open("datos.txt","w")
            f.write("Hola, soy HackerCloud")
            f.close()            
            Text2.configure(text=happy)
            ventana.config(bg="green")
            time.sleep(0.01)
            Text1.config(bg="green")
            time.sleep(0.01)
            Text2.config(bg="green")
        elif (queHacer.get() == "9"):
            f = open("datos.txt","w")
            f.write("Hola, soy HackerCloud")
            f.close()            
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
            time.sleep(0.01)
            f = open("datos.txt","w")
            f.write("SG9sYSwgc295IEhhY2tlckNsb3Vk")
            f.close()
            time.sleep(6)
            webbrowser.open("https://es.search.yahoo.com/search?p=how+to+create+your+onw+ramsomware&fr=yfp-t&fr2=p%3Afp%2Cm%3Asb&ei=UTF-8&fp=1")
            time.sleep(10)
            webbrowser.open("https://www.google.com/search?q=bonzi+buddy+is+a+virus%3F&sxsrf=AOaemvLD3mPh8p7ozCCgyzsGCVucD3bXOg%3A1642972559924&source=hp&ei=j8XtYZWENofqUqrfvYAK&iflsig=ALs-wAMAAAAAYe3TnzSms7z9nd4F0XB9Y9vZeUw_r3pz&ved=0ahUKEwjVh7ve5cj1AhUHtRQKHapvD6AQ4dUDCAg&uact=5&oq=bonzi+buddy+is+a+virus%3F&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHlAAWABg_QJoAHAAeACAAWWIAWWSAQMwLjGYAQCgAQKgAQE&sclient=gws-wiz")

    #función de opciones
    def Opciones():
        
        opciones = Tk()
        opciones.title("Opciones")
        opciones.geometry("500x250")
        opciones.config(bg="gray")
        opciones.resizable(0, 0)

        #function de matar todo
        def matarTodoF():
            time.sleep(0.01)
            opciones.destroy()

        #matar todo
        matarTodo = Button(opciones, command=matarTodoF, bg="red", text="X")
        matarTodo.place(x=465, y=0)

        #opciones texto
        texto1 = Label(opciones, bg="gray", text="1-Salir a pasear").place(x=150, y=10)
        texto1 = Label(opciones, bg="gray", text="2-Jugar con tu mascota").place(x=150, y=30)
        texto1 = Label(opciones, bg="gray", text="3-Salir al campo").place(x=150, y=50)
        texto1 = Label(opciones, bg="gray", text="4-Tratar mal a las personas").place(x=150, y=70)
        texto1 = Label(opciones, bg="gray", text="5-Estar con tu familia").place(x=150, y=90)
        texto1 = Label(opciones, bg="gray", text="6-Insultar al aire").place(x=150, y=110)
        texto1 = Label(opciones, bg="gray", text="7-Estar con tus amigos").place(x=150, y=130)
        texto1 = Label(opciones, bg="gray", text="8-Pensar en lo que no te gusta").place(x=150, y=150)
        texto1 = Label(opciones, bg="gray", text="9-Estar con personas que te caen bien").place(x=150, y=170)
        texto1 = Label(opciones, bg="gray", text="10-Tratar con agresividad a las cosas que te rodean").place(x=150, y=190)
        texto1 = Label(opciones, bg="gray", text="11-Repartir puñetazos por la calle").place(x=150, y=210)

    def Sintomas():

        sintomas = Tk()
        sintomas.title("Síntomas")
        sintomas.geometry("500x370")
        sintomas.resizable(0, 0)
        sintomas.config(bg="gray")

        #function de matar todo
        def matarTodoF():
            sintomas.destroy()

        #matar todo
        matarTodo = Button(sintomas, command=matarTodoF, bg="red", text="X")
        matarTodo.place(x=465, y=0)

        #texto síntomas
        sintomasTexto = Label(sintomas, bg="gray", text="Te vuelve agresivo").place(x=150, y=10)
        sintomasTexto = Label(sintomas, bg="gray", text="Te marea").place(x=150, y=30)
        sintomasTexto = Label(sintomas, bg="gray", text="Bulling").place(x=150, y=50)
        sintomasTexto = Label(sintomas, bg="gray", text="Impaciencia").place(x=150, y=70)
        sintomasTexto = Label(sintomas, bg="gray", text="Prepotencia").place(x=150, y=90)
        sintomasTexto = Label(sintomas, bg="gray", text="Adicción al móvil").place(x=150, y=110)
        sintomasTexto = Label(sintomas, bg="gray", text="Mentir compulsivamente").place(x=150, y=130)
        sintomasTexto = Label(sintomas, bg="gray", text="Violaciones").place(x=150, y=150)
        sintomasTexto = Label(sintomas, bg="gray", text="Sobreexigirse").place(x=150, y=170)
        sintomasTexto = Label(sintomas, bg="gray", text="Pesimismo").place(x=150, y=190)
        sintomasTexto = Label(sintomas, bg="gray", text="Inmadurez").place(x=150, y=210)
        sintomasTexto = Label(sintomas, bg="gray", text="Envidia").place(x=150, y=230)
        sintomasTexto = Label(sintomas, bg="gray", text="Vengativo").place(x=150, y=250)
        sintomasTexto = Label(sintomas, bg="gray", text="Racismo").place(x=150, y=270)
        sintomasTexto = Label(sintomas, bg="gray", text="Sexismo").place(x=150, y=290)
        sintomasTexto = Label(sintomas, bg="gray", text="Superficilidad").place(x=150, y=310)
        sintomasTexto = Label(sintomas, bg="gray", text="Pereza").place(x=150, y=330)
        sintomasTexto = Label(sintomas, bg="gray", text="*Adicción al móvil*").place(x=150, y=350)

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
    print('Ok')
    time.sleep(0.01)
    root.destroy()
#botones
ejecutar = Button(root, bg="white", height="1", width="2", command=SI, text="Si")
NoEjecutar = Button(root, bg="white", height="1", width="2", command=noEjecutar, text="No")
ejecutar.place(x=100, y=110)
NoEjecutar.place(x=180, y=110)



root.mainloop()
