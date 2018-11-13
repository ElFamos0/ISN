# coding: utf-8
# auteur: Oskar STAUDTE

# modules utilisés:
from tkinter import*


# fonctions qui definissent les differentes memes de chat à afficher


def ollie():
    photo0 = PhotoImage(file='seriouscat.gif')
    label.configure(image=photo0)
    label.image = photo0


def bongo():
    photo1 = PhotoImage(file='bongo.gif')
    label.configure(image=photo1)
    label.image = photo1


def longcat():
    photo2 = PhotoImage(file='longcat.gif')
    label.configure(image=photo2)
    label.image = photo2

# definiton de la fonction menu



# fenetre principale
fen = Tk()
fen.title("ObscureCatMemes")
fen.configure(bg="black")

photo = PhotoImage(file="seriouscat.gif")
label = Label(fen, image=photo)
label.pack()

b1 = Button(text="Polite cat", bg="Yellow", fg="Black", command=ollie)
b1.pack()

b2 = Button(text="Bongo cat", bg="Yellow", fg="Black", command=bongo)
b2.pack()

b3 = Button(text="Long cat", bg="Yellow", fg="Black", command=longcat)
b3.pack()


fen.mainloop()
