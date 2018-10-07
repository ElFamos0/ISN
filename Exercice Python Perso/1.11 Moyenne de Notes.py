# -*- coding : utf8 -*-
#Parfaitement Fonctionnel
note = int(input("Entrer vos notes (- qqch pour stop) : "))
notes = 0 
compteur = 0
while note>= 0:
	compteur += 1 
	notes += note
	note = int(input("Entrer vos notes (- qqch pour stop) : "))

print("La somme de ces notes est : ",notes)
if compteur>0:
	print("La moyenne de ces notes est : ",notes/compteur) 
else:
	print("Me prend pas pour un jambon")
