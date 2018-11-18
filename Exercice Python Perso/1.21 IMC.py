# -*- coding : utf8 -*-

'''
	Auteur : MDTech
	Titre : IMC 
	Création : 25/10/2018
	Stade : Terminé
'''

import os

P = eval(input("Entrez votre poids (en kg) : "))
T = eval(input("Entrez votre taille (en m) : "))

IMC = round(P / (T**2), 1)
print("Votre IMC est de : ", IMC, "kg/m^2")
if IMC < 25:
    print("Tout va bien ! Vous avez un poids idéal pour votre taille")
elif IMC >= 25 and IMC <= 30:
    print("Vous êtes en surpoid vous ferez mieux de faire un peu d'exercice")
elif IMC >= 30:
    print("Vous êtes obèse; votre santé est menacé")
os.system("pause")
