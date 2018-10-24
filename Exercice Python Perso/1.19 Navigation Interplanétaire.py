# -*- coding : utf8 -*-
#Navigation Interplanétaire
from math import sqrt
d = eval(input("La distance qui sépare le Soleil de la planète visée "))
T = round((365.25/2)*sqrt((1+d)**3/8.0))
if T<365:
	print("Temps de Navigation Interplanétaire \n Jour :",T)
if T>365:
	a = int(T/365)
	j = int(T)%365
	if a<1:
		print("Temps de Navigation Interplanétaire \n Jour :",j)
	else:
		print("Temps de Navigation Interplanétaire \n Années :",a,"\nJour : ",j)