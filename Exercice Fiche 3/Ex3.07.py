#coding: utf-8
liste = [9,5,5,7,4,8,2,8,1,9]
liste2 = []
for i in range(0, len(liste)-1):
    if liste[i] in liste2:
        pass
    else:
        liste2.append(liste[i])
liste2.sort()
print(liste2)