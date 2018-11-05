# -*- coding : utf8 -*-
'''
	Auteur : MDTech
	Titre : Triangle Rectangle ?
	Stade: Terminé
'''
a = eval(input("a = "))
b = eval(input("b = "))
c = eval(input("c = "))

R1 = a**2 == b**2 + c**2
R2 = b**2 == a**2 + c**2
R3 = c**2 == a**2 + b**2 

if R1 == True or R2 == True or R3 == True:
	print("Ces côtés forment un triangle rectangle")
else:
	print("Ces côtés ne forment pas de triangle rectangle+")