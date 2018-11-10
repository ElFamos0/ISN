# coding: utf-8

'''
Auteur : Malo Damien
'''

from tkinter import*

#Fonctions

def Effacer():
    s1.delete(0, last=END)
    s2.delete(0, last=END)

def Valider():
    for i in fen.winfo_children():
        i.grid_forget()
    l3 = Label(text="Vos données ont bien été envoyé")
    l3.place(x=10,y=20)




#Programme Principal

fen = Tk()
fen.title("Malo")
fen.geometry("200x80")
l1 = Label(text="Nom : ")
l1.grid(column=1, row=4)
l2 = Label(text="Tel : ")
l2.grid(column=1, row=8)
s1 = Entry(width=25)
s1.grid(column=2, row=4, columnspan=2)
s2 = Entry(width=25)
s2.grid(column=2, row=8, columnspan=2)
but1 = Button(text="Effacer",command=Effacer)
but1.grid(column=2,row=9,sticky="E")
but2 = Button(text="Valider",command=Valider)
but2.grid(column=3,row=9,sticky="W")


fen.mainloop()
