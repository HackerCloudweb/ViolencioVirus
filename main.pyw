from ast import If
from cProfile import label
from collections import deque
from struct import pack
from tkinter import messagebox
from tkinter.ttk import *
from sqlite3 import Row
from tkinter import *
import tkinter as tk
from tkinter import font
import webbrowser
import time
import os
import webbrowser as wb

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
    Text1M = Label(ventana, bg="gray", text="Estoy enfadado, ¿Qué puedo hacer para que se me pase?")
    Text1M.place(x=60, y=40)
    Text2M = Label(ventana, bg="gray", text=angry)
    Text2M.configure(font=(20))
    Text2M.place(x=225, y=60)

    
    #Input
    queHacer = Entry(ventana, text="Que hacer")
    queHacer.place(x=155, y=80)

    #función de probar
    def Probar():

        if (queHacer.get() == "1"):
            f = open("archivos/datos.txt","w")
            f.write("Hola, soy HackerCloud")
            f.close()
            Text2M.configure(text=happy)
            ventana.config(bg="green")
            time.sleep(0.01)
            Text1M.config(bg="green")
            time.sleep(0.01)
            Text2M.config(bg="green")
            time.sleep(0.01)
            webbrowser.open("https://www.champcueil.fr/wp-content/uploads/2015/11/%C2%A1estoy-bien.png")
        elif (queHacer.get() == "0"):
            f = open("archivos/datos.txt","w")
            f.write("Hola, soy HackerCloud")
            f.close()
            time.sleep(0.01)
            Text2M.configure(text=angry)    
            time.sleep(0.01)
            ventana.config(bg="gray")        
            time.sleep(0.01)
            Text1M.configure(bg="gray")
            time.sleep(0.01)
            Text2M.configure(bg="gray")
            time.sleep(0.01)
            webbrowser.open("https://www.champcueil.fr/wp-content/uploads/2015/11/%C2%A1estoy-bien.png")
        elif (queHacer.get() == "2"):
            f = open("archivos/datos.txt","w")
            f.write("Hola, soy HackerCloud")
            f.close()
            Text2M.configure(text=happy)
            ventana.config(bg="green")
            time.sleep(0.01)
            Text1M.config(bg="green")
            time.sleep(0.01)
            Text2M.config(bg="green")
            time.sleep(0.01)
            webbrowser.open("https://www.champcueil.fr/wp-content/uploads/2015/11/%C2%A1estoy-bien.png")
        elif (queHacer.get() == "3"):
            f = open("archivos/datos.txt","w")
            f.write("Hola, soy HackerCloud")
            f.close()            
            Text2M.configure(text=happy)
            ventana.config(bg="green")
            time.sleep(0.01)
            Text1M.config(bg="green")
            time.sleep(0.01)
            Text2M.config(bg="green")
            time.sleep(0.01)
            webbrowser.open("https://www.champcueil.fr/wp-content/uploads/2015/11/%C2%A1estoy-bien.png")
        elif (queHacer.get() == "5"):
            f = open("archivos/datos.txt","w")
            f.write("Hola, soy HackerCloud")
            f.close()            
            Text2M.configure(text=happy)
            ventana.config(bg="green")
            time.sleep(0.01)
            Text1M.config(bg="green")
            time.sleep(0.01)
            Text2M.config(bg="green")
            time.sleep(0.01)
            webbrowser.open("https://www.champcueil.fr/wp-content/uploads/2015/11/%C2%A1estoy-bien.png")
        elif (queHacer.get() == "7"):
            f = open("archivos/datos.txt","w")
            f.write("Hola, soy HackerCloud")
            f.close()            
            Text2M.configure(text=happy)
            ventana.config(bg="green")
            time.sleep(0.01)
            Text1M.config(bg="green")
            time.sleep(0.01)
            Text2M.config(bg="green")
            time.sleep(0.01)
            webbrowser.open("https://www.champcueil.fr/wp-content/uploads/2015/11/%C2%A1estoy-bien.png")
        elif (queHacer.get() == "9"):
            f = open("archivos/datos.txt","w")
            f.write("Hola, soy HackerCloud")
            f.close()            
            Text2M.configure(text=happy)
            ventana.config(bg="green")
            time.sleep(0.01)
            Text1M.config(bg="green")
            time.sleep(0.01)
            Text2M.config(bg="green")
            time.sleep(0.01)
            webbrowser.open("https://www.champcueil.fr/wp-content/uploads/2015/11/%C2%A1estoy-bien.png")
        else:
            Text1M.configure(bg="red")
            Text2M.configure(text=superAngry, bg="red")
            ventana.config(bg="red")
            time.sleep(0.01)
            f = open("archivos/datos.txt","w")
            f.write("SG9sYSwgc295IEhhY2tlckNsb3Vk")
            f.close()
            time.sleep(10)
            youser = open ('archivos/jeje.txt','w')
            youser.write('\n \n ME HE ENFADADO MÁS, \n \n TU PC NO VOLVERÁ A ENCENDER, \n \n DISFRUTALO CUANDO PUEDAS :)')
            youser.close()
            time.sleep(0.01)
            os.system("open" + " archivos/jeje.txt")
            time.sleep(3)
            
            def dequevas():

                ancho_dequevas = 300
                alto_dequevas = 150

                dequevas = Tk()
                dequevas.title("Lol")
                dequevas.geometry("300x150")
                dequevas.resizable(0, 0)
                dequevas.config(bg="red")

                x_dequevas = dequevas.winfo_screenwidth() // 2 - ancho_dequevas // 2
                y_dequevas = dequevas.winfo_screenheight() // 2 - alto_dequevas // 2

                posicion = str(ancho_dequevas) + "x" + str(alto_dequevas) + "+" + str(x_dequevas) + "+" + str(y_dequevas)
                dequevas.geometry(posicion)

                Label(dequevas, bg="red", text="\n \n \n \n f`f1�f�{f�{fRfPSjj��f�6�{����Œ�6�{��A���{��dfa�� \n f`f1�f�{f�{fRfPSjj��f�6�{����Œ�6�{��A���{��dfa��??").pack()

            def dequevas2():

                ancho_dequevas2 = 300
                alto_dequevas2 = 150

                dequevas2 = Tk()
                dequevas2.title("Lol")
                dequevas2.geometry("300x150")
                dequevas2.resizable(0, 0)
                dequevas2.config(bg="orange")

                x_dequevas2 = dequevas2.winfo_screenwidth() // 2 - ancho_dequevas2 // 2
                y_dequevas2 = dequevas2.winfo_screenheight() // 2 - alto_dequevas2 // 2

                posicion = str(ancho_dequevas2) + "x" + str(alto_dequevas2) + "+" + str(x_dequevas2) + "+" + str(y_dequevas2)
                dequevas2.geometry(posicion)

                Label(dequevas2, bg="orange", text="\n \n \n \n f`f1�f�{f�{fRfPSjj��f�6�{����Œ�6�{��A���{��dfa�� \n f`f1�f�{f�{fRfPSjj��f�6�{����Œ�6�{��A���{��dfa��¿¿").pack()

            time.sleep(10)

            dequevas()
            dequevas2()
            dequevas()
            dequevas2()
            dequevas()
            dequevas2()
            dequevas()
            dequevas2()

            time.sleep(20)
            webbrowser.open("https://hackercloudweb.github.io/img/paloma-edit.png")
            time.sleep(7)
            os.system("firefox")
            time.sleep(10)
            webbrowser.open("https://es.unesco.org/commemorations/peaceday")
            time.sleep(9)
            os.system("gnome-terminal")
            time.sleep(14)
            webbrowser.open("https://duckduckgo.com/?q=D%C3%ADa+internacional+de+la+paz&t=ffab&ia=web")
            time.sleep(9)
            os.system("chromium")
            time.sleep(10)
            f = open("/home/david/Desktop/hola.txt", "w")
            f.write("SG9sYSwgc295IHZpb2xlbmNpb3ZpcnVz")
            f.close()
            time.sleep(50)
            os.system("reboot")





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
