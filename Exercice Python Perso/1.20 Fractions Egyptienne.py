# -*- coding : utf8 -*-
'''
	Auteur : Malo
	Titre : Fraction Egyptienne
	Stade : Terminé
'''
from fractions import Fraction

def egyptation(a,b):
	q = 1 + int(b/a)
	F = Fraction(1,q)
	return F

def comparaison(x):
	num = x.numerator
	if num == 1:
		print("Décomposition Complète")
	else:
		print("Décomposition Incomplète (On taff dessus encore)")

print("Donner le numérateur a et le dénominateur b d'une fraction (!! attention il faut que b>a)")
a = eval(input("a = "))
b = eval(input("b = "))
while a>b:
	print("Vous n'avez pas suivi la consigne")
	a = eval(input("a = "))
	b = eval(input("b = "))


F0 = Fraction(a,b)

F1 = egyptation(a,b)

F2 = F0-F1
 
comparaison(F2)
print(F0,"=",F1,"+",F2)

