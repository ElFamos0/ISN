# coding: utf-8
# Petit Module Utilisés
from tkinter import*
import pygame

pygame.init()

# La jeune fonction


def say_bitconnect():
    son.play()


# Caractéristiques de la fenètre
fen = Tk()
fen.title("BITCONNNNEEEECTTTT")
fen.configure(bg="black")

# Integration de l'image so bitconnect
photo = PhotoImage(file='bitconnect.gif')
label = Label(fen, image=photo)
label.pack()

# Le petit bouton de la muerte    si tu lis ça oskar tu es une petite salope <3
Bouton = Button(text="BITCOOONNNEEECTTT", bg="orange", command=say_bitconnect)
Bouton.pack()

# Le doux son a tes oreilles josé
son = pygame.mixer.Sound("BITCONNECT.wav")


fen.mainloop()
