# -*- coding : utf8 -*-
print("Entrer dans cet ordre votre date : Année Mois Jour (Avec un espace entre chaque nombre et que des nombres")
lol = input()
lol = lol.split(" ")
try : 
	A = int(lol[0]) 
	M = int(lol[1])
	J = int(lol[2])
	c = (14-M)//12
	a = int(A-c)
	m = int(M+12*c)-2
	R1 = (a//4)+(a//400)+((31*m)//12)-(a//100)
	R2 = R1+J+a
	j = R2%7

	jours_de_la_semaine = ["Dimanche","Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi"]

	print("Ce jour était un",jours_de_la_semaine[j]) 
except:
	print("Suis les consignes s'il te plait")
