# -*- coding: utf-8 -*

def conversionheure(h,m,s):
  h = 3600*h
  m = 60*m
  return(h+m+s)

def différencedetemps(o,i):
	"Calcul une différence de temps entre deux horaires"
	return abs(o-i)

print(différencedetemps(conversionheure(1,0,0),conversionheure(2,0,0)))