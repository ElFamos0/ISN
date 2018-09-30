# -*- coding : utf8 -*-
'''
	Auteur : Malo 
	Programme : Scrabble Eco+ Edition
	Enonce : On place dans une chaîne 7 lettres correspondant au tirage du jeu d’un joueur au Scrabble. Réaliser un programme qui
	demande au joueur un mot et lui dit s’il peut en effet le former avec ses 7 lettres.
'''
'''
1 point : E ×15, A ×9, I ×8, N ×6, O ×6, R ×6, S ×6, T ×6, U ×6, L ×5
2 points : D ×3, M ×3, G ×2
3 points : B ×2, C ×2, P ×2
4 points : F ×2, H ×2, V ×2
8 points : J ×1, Q ×1
10 points : K ×1, W ×1, X ×1, Y ×1, Z ×1
Pour un total de 100 jetons 
'''
from random import randint

a = "AAAAAAAAABBCCDDDEEEEEEEEEEEEEEEFFGGHHIIIIIIIIJKLLLLLMMMNNNNNNOOOOOOPPQRRRRRRSSSSSSTTTTTTUUUUUUVVWXYZ"
Scrabble = list(a)
lettreschoisies = []

for i in range(0,7):
	b = randint(0,len(a)-1)
	lettreschoisies += a[b]

print("Voici votre tirage : ",lettreschoisies)

rep = input("Quel mot pouvez vous former avec ces lettres ? : ").upper()

if rep in lettreschoisies:
	print("Oui c'est ça")
else:
	print("Non ce n'est pas dans la liste de lettre ")
