# -*- coding: utf-8 -*
#on importe la racine carré du module de math.
from math import sqrt
#on entre les différentes variables du trinome
a = float(input("Entrer la valeur a du trinôme"))
b = float(input("Entrer la valeur b du trinôme"))
c = float(input("Entrer la valeur c du trinôme"))
#on effectue le calcul du discriminant
discriminant = b**2 - 4*a*c
'''
procédure pour chercher les racines si le discriminant est positif ou la
racine si le discriminant est nul. Si le discriminant est négatif affiche qu'il
n'y a pas de racines

'''
if discriminant > 0 :
    x1 = (-b-sqrt(discriminant))/2*a
    x2 = (-b+sqrt(discriminant))/2*a
    print ("Le discriminant est égal à",discriminant,
    "Il est donc positif\nLe trinome possède donc deux racines :",x1,"et",x2 )
elif discriminant==0:
    x0 = -b/2*a
    print("Le discriminant est égal à 0 \nLe trinome possède donc une racine :",x0 )
else :
    print("Le discriminant est égal à",discriminant,
    "Il est donc négatif \nIl n'existe pas de racines pour ce trinôme")
