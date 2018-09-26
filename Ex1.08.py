liste = []
lol = False
while lol==False:
    a = int(input("Nombre : "))
    if a in liste:
        lol = True
    else:
        liste.append(a)
print("Vous avez entré deux fois le même nombre")
print("La somme des nombres est",sum(liste))
print("Le maximum est",max(liste))
print("Le minimum est",min(liste))
print("Le rang du max est:",liste.index(max(liste)))
print("Le rang du min est:",liste.index(min(liste)))