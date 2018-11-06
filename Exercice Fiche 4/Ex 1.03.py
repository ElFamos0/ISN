# -*- coding: utf-8 -*
from math import pi
def AireDisque(x):
    "Calcule l'aire d'un disque"
    return(round((pi*x*x),2))
def VolumeCylindre(A,h):
    "Calcule le Volume d'un cylindre avec Aire de la base et hauteur"
    return(AireDisque(A)*h)
print(round(VolumeCylindre(5,7),2))
