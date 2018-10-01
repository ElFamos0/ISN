# -*- coding : utf8 -*-

'''
	Auteur : Mada 
	Programme : Calcule le prix TTC à partir d'un HT
'''

PrixHT = float(input("Le prix hors taxe (taper 0 pour terminer le programme) : "))

while PrixHT>0:
	print("Le prix TTC est :",(PrixHT*1.196),"€")
	PrixHT = float(input("Le prix hors taxe (taper 0 pour terminer le programme) : "))

print("TY BITCH")
