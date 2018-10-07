# -*- coding : utf8 -*-
'''Ecrire un programme qui détermine si un entier N est parfait ou non. Un entier est dit parfait s'il est égal à la somme de ses diviseurs. Exemple 6 = 3 + 2 +1'''
from math import ceil,sqrt
from math import *
N =int ( input ("saisir un nombre"))
S =1
for i in range (2 , ceil ( sqrt ( N ))+1) :
    if N % i ==0 :
        S += i
if S == N :
    print (N ,"est un nombre parfait ")

