# -*- coding : utf8 -*-
'''
	Auteur : MDTech
	Titre : Année Bissextile 
	Stade: Terminé
'''
ann = int(input("Entrez une année : "))

r1 = ann%4
r2 = ann%100
r3 = ann%400

if r1 == 0 and r2 != 0:
	print("Année Bissextile")
if r3 == 0:
	print("Année Bissextile")
if r1 != 0:
	print("Année non Bissextile")
if r2 ==0 and r3 != 0:
	print("Année non Bissextile")