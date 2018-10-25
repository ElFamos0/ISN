# -*- coding : utf8 -*-

#Tp n°1
from math import sqrt, floor
R = 6400
c = 1.316926e11
h = eval(input("Entrer la distance à laquelle est lancée le satellite : "))
T = sqrt((R+h)**3/c)
H  = int(T)
M = floor(60*(T-int(T)))
print("La période de révolution pour un satellite lancée à",h,"km\nT = ",H,"h",M,"min")


