# -*- coding: utf-8 -*

'''
	Auteur : Malo
'''

def conversionheure(h,m,s):
	"Fonction qui fait une conversion d'un temps donné en heure, minute, seconde en seconde"
	h = 3600*h
 	m = 60*m
 	return(h+m+s)
print("En tout il y a",conversionheure(1,2,0),"secondes")

