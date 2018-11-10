from tkinter import *
Fenetre=Tk()
Fenetre.title("Mon programme en Tkinter")
# Donne un titre à la fenêtre
zone_dessin = Canvas(Fenetre,width=500,height=500,bg='yellow')
zone_dessin.pack() #Affiche le Canvas
zone_dessin.create_line(0,0,500,500,fill='red',width=2)
# Dessine une ligne
zone_dessin.create_line(0,500,500,0,fill='red',width=2)
# Dessine une ligne
zone_dessin.create_rectangle(150,150,350,350)
# Dessine un carré
zone_dessin.create_oval(150,150,350,350,fill='blue',width=4)
# Dessine un cercle
# bouton_sortir est un widget de type "Button"
bouton_sortir= Button(Fenetre,text="Sortir",command=Fenetre.destroy)
# la commande "destroy" appliquée à la fenêtre détruit l'objet "Fenetre" et clôture le programme
bouton_sortir.pack()
Fenetre.mainloop()