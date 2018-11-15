from tkinter import*

fen = Tk()
dessin = Canvas(fen, width=400, height=400, bg="grey")
dessin.pack()
for i in range(1, 21):
    dessin.create_line(0, (400 - (i * 20)), (400 - (i * 20)), (400 - i), width=2, fill="red")


fen.mainloop()
