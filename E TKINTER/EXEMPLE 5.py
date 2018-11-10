from tkinter import *
racine=Tk()
photo=PhotoImage(file="andromede2.gif") # création d'un objet de la classe PhotoImage
racine.geometry("800x600") #détermination de la taille de la fenêtre principale
racine.title("800x600")
fond=Canvas(racine, bg='blue',width=600,height=300)
fond.pack(side=LEFT)
img=fond.create_image(400,100,image=photo)
for i in range(1,6):
    fond.create_line(i*100,0,i*100,300)
for i in range(1,3):
    fond.create_line(0,i*100,600,i*100)
racine.mainloop()