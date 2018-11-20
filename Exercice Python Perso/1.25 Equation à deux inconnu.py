# -*- coding : utf8 -*-

'''
	Auteur : MDTech
	Titre :  Equation à deux inconnu
	Création : 30/10/2018
	Stade : terminé
'''

a = eval(input("Entrez a : "))
b = eval(input("Entrez b : "))
c = eval(input("Entrez c : "))
A = eval(input("Entrez A : "))
B = eval(input("Entrez B : "))
C = eval(input("Entrez C : "))

if (a * B) - (A * b) != 0:
    x = (B * c - b * C) / (a * B - A * b)
    y = (a * C - A * c) / (a * B - A * b)
    print("x =", x)
    print("y = ", y)
if (a * B - A * b) == 0 and (c * A - C * a) == 0
    print("Le système est indéterminé")
if (a * B - A * b) == 0 and (c * A - C * a) != 0:
    print("Le système n'a pas de solution")
print("Fin du programme")
