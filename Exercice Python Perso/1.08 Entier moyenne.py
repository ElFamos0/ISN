# -*- coding : utf8 -*-

nbr = int(input("Entrer un nombre entier : (négatif pour arrêter)"))
somme = 0
compteur = 0
while nbr >= 0:
    somme += nbr
    nbr = int(input("Entrer un nombre entier : (négatif pour arrêter)"))
    compteur += 1
print("La somme des entiers :",somme)
moyenne = somme/compteur
print(moyenne)
