from tkinter import*
fen = Tk()
fen.title("Malo")
dessin = Canvas(fen, width=400, height=400, bg="grey")
dessin.pack()


# Les bonnes grosses lignes

for i in range(20):
    dessin.create_line(0, 20 * i, 20 * i, 400, fill="red", width=2)
    dessin.create_line(20 * i, 0, 400, 20 * i, fill="blue", width=2)
    dessin.create_line(400, 20 * i, 400 - (20 * i), 400, fill="purple", width=2)
    dessin.create_line(0, i * 20, 400 - (20 * i), 0, fill="yellow", width=2)

fen.mainloop()
