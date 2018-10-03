# coding: utf-8

liste = range(30,101)
carre = []
cube = []

for i in range(0,len(liste)):
    carre.append(liste[i]**2)
    cube.append(liste[i]**3)

print(carre)
print(cube)

