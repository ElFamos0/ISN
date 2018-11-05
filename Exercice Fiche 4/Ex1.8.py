# -*- coding: utf-8 -*

def conversionheure(h,m,s):
  h = 3600*h
  m = 60*m
  return(h+m+s)
print("En tout il y a",conversionheure(1,2,0),"secondes")

