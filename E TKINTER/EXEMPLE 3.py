from tkinter import *
fen=Tk()
# création de la fenêtre principale
f=Frame(fen,bg="blue" )
#création de la sous-fenêtre f
l=Label(f,text="label 1")
#le premier paramêtre correspond à la sous-fenêtre dans laquelle sera l
l.pack()
#placement de l dans f
s=Entry(f,width=10)
s.pack()
f.pack(side=LEFT)
#ajout de f àla fenêtre principale
l2=Label(text="label 2")
l2.pack(side=RIGHT)
fen.mainloop()