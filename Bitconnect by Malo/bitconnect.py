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
photo = PhotoImage(file='titlescreen.png')

label = Label(fen, image=photo)
label.grid(row=1, column=1, columnspan=2)


# Le petit bouton de la muerte    si tu lis ça oskar tu es une petite salope <3
Bouton = Button(text="BITCOOONNNEEECTTT", bg="orange", command=say_bitconnect)
Bouton.grid(row=2, column=1, sticky="W")
Bouton2 = Button(text="chickens", bg="red")
Bouton2.grid(row=2, column=2, sticky="E")

# Le doux son a tes oreilles josé
son = pygame.mixer.Sound("SONS\\BITCONNECT.wav")
son2 = pygame.mixer.Sound("SONS")

fen.mainloop()
