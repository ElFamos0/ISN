# -*- coding : utf8 -*-

nbr = int(input("Rentrer un nombre : "))
F = 1

for i in range(2,nbr+1):
	F *= i
print("Factoriel de",nbr,"est :",F)