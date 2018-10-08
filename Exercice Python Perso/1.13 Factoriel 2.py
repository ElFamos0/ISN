# -*- coding : utf8 -*-

a = int(input("Entrer un nombre : "))
compteur = 2
F=1
while compteur <= a:
	F *= compteur
	compteur += 1

print(F)
