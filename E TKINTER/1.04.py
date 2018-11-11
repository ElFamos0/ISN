# coding: utf-8

from tkinter import*

fen = Tk()
fen.title("Malo")
dessin = Canvas(fen, width=400, height=400, bg="grey")
dessin.pack()


# Les bonnes grosses lignes

for i in range(20):
    dessin.create_line(0, (400 - i + 1 * 20), 400, (400 - i * 20), fill="red", width=2)

fen.mainloop()
