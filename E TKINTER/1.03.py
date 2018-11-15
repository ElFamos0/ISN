# coding: utf-8
from tkinter import*

# Fonctions


def Valider():
    for i in fen.grid_slaves():
        i.destroy()
    l3 = Label(text="Merci pour ces infos")
    l3.place(x=40, y=25)


def Effacer():
    s1.delete(0, END)
    s2.delete(0, END)


# Programme Principal
fen = Tk()
fen.title("Malo")
fen.geometry("200x80")
l1 = Label(text="Nom : ")
l1.grid(column=1, row=2)
l2 = Label(text="Tel : ")
l2.grid(column=1, row=4)
s1 = Entry(width=25)
s1.grid(column=2, row=2, columnspan=2)
s2 = Entry(width=25)
s2.grid(column=2, row=4, columnspan=2)
b1 = Button(text="Effacer", command=Effacer)
b1.grid(column=2, row=6, sticky="E")
b2 = Button(text="Valider", command=Valider)
b2.grid(column=3, row=6, sticky="W")


fen.mainloop()
