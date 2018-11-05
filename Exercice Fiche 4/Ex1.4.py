# -*- coding: utf-8 -*

def fact(n):
    "Calcule la factorielle de n"
    somme = 1
    for i in range(1,n+1):
        somme *= i
    return somme
n = int(input("Calculer factorielle de : "))
print(fact(n))