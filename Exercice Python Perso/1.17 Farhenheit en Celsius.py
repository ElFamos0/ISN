# -*- coding : utf8 -*-

def ConvertirenFahrhenheit(c):
	Fahrhenheit = round((c*1.8)+32,1)
	return Fahrhenheit

def ConvertirenCelsius(f):
	Celsius = round((f-32)/1.8,1)
	return Celsius

print("Convertisseur de température \nChoississez votre mode \n 0 : Celsius en Fahrhenheit \n 1 : Fahrhenheit en Celsius")
a = int(input("Votre choix : "))
if a == 0:
	c = eval(input("Rentrer votre température en Celsius : " ))
	print(ConvertirenFahrhenheit(c))
elif a == 1:
	f = eval(input("Rentrer votre température en Fahrhenheit : " ))
	print(ConvertirenCelsius(f)) 
else:
	print("Vous n'avez pas suivi les consignes")