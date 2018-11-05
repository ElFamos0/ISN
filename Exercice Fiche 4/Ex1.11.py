# -*- coding: utf-8 -*

def PremierMot(x):
	"Renvoit le premier mot d'une chaine de caractère x"
	lol = x.split(" ")
	return lol[0]
x = input("Rentrer une phrase")
print("Le Premier mot de",x,"est : ",PremierMot(x))