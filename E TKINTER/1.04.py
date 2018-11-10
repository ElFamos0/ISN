# coding: utf-8

from tkinter import*

fen = Tk()
fen.title("Malo")
dessin = Canvas(fen, width=400, height=400, bg="grey")
dessin.pack()


l = dessin.create_line(0, 0, 200, 200, fill="red", width=10)
fen.mainloop()
