# -*- coding : utf8 -*-
a = eval(input("Entrer la mesure en degré de l'angle entier : "))

if int(a) == a:
	n  = 360/(180-a)
	if n == int(n):
		print("Polygone de",int(n),"côtées")
	else:
		print("Ce n'est pas un polygone régulier") 
else:
	print("Entrer un entier plz")