# -*- coding : utf8 -*-
n = eval(input("Combien de côtés ? : "))
if int(n) == n:							#C'est interessant pour que l'utilisateur ne tombe pas sur une erreur si il rentre des décimales. 
	a = 180*(n-2)//n
	print("Angle de",a,"°")
else:
	print("Entrer un nombre de coté sivouplé") 