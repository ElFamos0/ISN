# coding: utf-8
from tkinter import*
x1, y1, x2, y2 = 300, 150, 315, 165


def go_up():
    global y1, y2
    y1 -= 10
    y2 -= 10
    ecran.create_oval(x1, y1, x2, y2, fill="yellow")


def go_down():
    global y1, y2
    y1 += 10
    y2 += 10
    ecran.create_oval(x1, y1, x2, y2, fill="yellow")


def go_left():
    global x1, x2
    x1 -= 10
    x2 -= 10
    ecran.create_oval(x1, y1, x2, y2, fill="yellow")


def go_right():
    global x1, x2
    x1 += 10
    x2 += 10
    ecran.create_oval(x1, y1, x2, y2, fill="yellow")


fen = Tk()
fen.title("Malo")
fen.configure(bg="blue")
ecran = Canvas(fen, width=600, height=300, bg="grey")
ecran.create_oval(300, 150, 315, 165, fill="yellow")


ecran.pack()


commandes = Frame(fen, width=600, height=100, bg="blue")
bouton_haut = Button(commandes, text="Haut", command=go_up)
bouton_haut.grid(column=2, row=1)
bouton_gauche = Button(commandes, text="Gauche", command=go_left)
bouton_gauche.grid(column=1, row=2)
bouton_droite = Button(commandes, text="Droite", command=go_right)
bouton_droite.grid(column=3, row=2)
bouton_bas = Button(commandes, text="Bas", command=go_down)
bouton_bas.grid(column=2, row=3)
commandes.pack()
fen.mainloop()
