# -*- coding : utf8 -*-
'''
	auteur : MDTech
	Titre : Divisible par 5 ou 3
	Stade: Terminé
'''

nbr = eval(input("Entrez un nombre : "))

r1 = nbr%3
r2 = nbr%5

if r1 == 0 and r2 == 0:
	print("Nombre divisible par 3 et par 5")
elif r1 == 0 and r2 != 0:
	print("Nombre divisible par 3 mais pas par 5")
elif r1 != 0 and r2 == 0:
	print("Nombre divisible par 5 mais pas par 3")
elif r1 != 0 and r2 =! 0:
	print("Nombre divisible ni par 3 ni par 5")