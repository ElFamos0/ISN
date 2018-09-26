# -*- coding: utf-8 -*

'''
Auteur : Malo Damien
Programme : Juste Prix
'''
def comparaison(rep):
    global win,nbralea,c
    if rep == nbralea:
        print("BRAVO VOUS AVEZ GAGNE")
        win = True
    elif rep >= nbralea:
        print("PLUS PETIT QUE",rep)
        c=+1
    else :
        print("PLUS GRAND QUE",rep)
        c=+1

from random import randrange
nbralea = randrange(10000,40001)
win = False
c = 0
for i in range(1,21):
    if win == False:
    	rep1 = int(input("Proposition n°"))
    	comparaison(rep1)
    else:
        break
print("Fin du juste prix vous avez gagné en",c,"tentative")

