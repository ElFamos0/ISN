# -*- coding : utf8 -*-
from math import pi
# Nous cherchons a calculer le volume d'un cone droit

rayon = float(input("Entrer le rayon de votre cône"))
hauteur = float(input("Entrer la hauteur de votre cône"))

volume = (pi * (rayon**2) * hauteur) / 3.0
print(volume)
