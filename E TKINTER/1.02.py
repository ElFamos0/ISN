# -*- coding : utf8 -*-
from random import*
from tkinter import*
# FONCTION


def var1et100():
    global compt
    var = int(entree.get())
    compt -= 1
    if var == a:
        l1.config(text="Bravo ! Tu as trouvé ! Le nb était " + str(a))
        bouton.destroy()
    elif var > a:
        l1.config(text="Trop grand.")
        l2.config(text="Il reste" + str(compt) + "essai")
    elif var < a:
        l1.config(text="Trop petit.")
        l2.config(text="Il reste" + str(compt) + "essai")
    if compt < 0:
        l1.config(text="Perdu")
        l2.config(text="")
        bouton.destroy()


# PROGRAMME PRINCIPAL
fen = Tk()
fen.title("Malo")
compt = 6
a = randint(1, 100)
regle = Label(text="Propose un nb entre 1 et 100")
regle.pack()
entree = Entry(bg="white", fg="black", width=20)
entree.pack()
bouton = Button(text="Tester", command=var1et100)
bouton.pack()
l1 = Label(text=" ")
l1.pack()
l2 = Label(text=" ")
l2.pack()
fen.mainloop()
