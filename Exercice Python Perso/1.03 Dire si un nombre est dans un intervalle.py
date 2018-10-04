# -*- coding : utf8 -*-

interA = int(input("Saisir [a,b] [a = : "))
interB = int(input("Saisir [a,b] b] = : "))
nbr = int(input("Donner un nombre : "))

if interA<= nbr<=interB:
    print("Ce nombre est compris dans l'intervalle")
else:
    print("Ce nombre n'est pas compris dans l'intervalle")

