# -*- coding : utf8 -*-
from math import sqrt
xa = int(input("Coordonnée xA"))
ya = int(input("Coordonnée yA"))
xb = int(input("Coordonnée xB"))
yb = int(input("Coordonnée yB"))
AB = sqrt((xb-xa)**2 + (yb-ya)**2)
print (AB)