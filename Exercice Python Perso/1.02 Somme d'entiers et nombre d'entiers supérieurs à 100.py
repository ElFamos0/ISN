# -*- coding : utf8 -*-

Somme, nombredetermes, morethan100, = 0, 0, 0

x = int(input("Entrer un nombre entier (0 pour arrêter le programme): "))

while x > 0:
    Somme += x
    nombredetermes += 1
    if x >= 100:
        morethan100 += 1
    x = int(input("Entrer un nombre entier (0 pour arrêter le programme)"))

print("\n Somme =", Somme)
print("Vous avez entré", nombredetermes, "nombres. Dont", morethan100, "étaient supérieur ou égal à 100")
