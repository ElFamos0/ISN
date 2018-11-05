# -*- coding: utf-8 -*
def fact(n):
    "Calcule la factorielle de n"
    produit = 1
    for i in range(1,n+1):
        produit *= i
    return produit

def C(n,p):
    "C(n,p) = n! / p!(n-p)!"
    valeur = fact(n)/fact(p)*fact(n-p)
    return valeur

print(C(4,5))
