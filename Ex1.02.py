# -*- coding : utf8 -*-
xa = int(input("xa"))
ya = int(input("ya"))
xb = int(input("xb"))
yb = int(input("yb"))
xi = (xa + xb)/2
yi = (ya + yb)/2
print("Coordonnés I (",xi,";",yi,")")
if ya != yb:
    print("Coupe l'axe des abscisse")
    xm = xa - (ya*(xb-xa))/(yb-ya)
    print("les coordonnés du point d'intersection est (",xm,"; 0)")
else :
    print("coupe pas l'axe des abscisse")