# -*- coding: utf-8 -*
from tkinter import *
#FONCTION

def AireDuCarre():
    global c # c représente le côté du carré
    c=int(e.get())
    aire=c*c
    l2.config(text="la surface du carré de côté "+str(c)+" est "+str(aire)) # je modifie le texte du label que j’ai appelé l2
#PROGRAMME PRINICIPAL
fen=Tk()
titre = "côté"
l=Label(text=titre) #le texte du label est le contenu de la variable nb
l.pack()
e = Entry(bg="white",fg="black",width=20)
e.pack()
b=Button(text="calculer",command=AireDuCarre) # la fonction plus est associée au clic sur le bouton
b.pack()
salut = ""
l2=Label(text=salut)
l2.pack()

fen.mainloop()