# -*- coding : utf8 -*-
Palin = input("Entrer un palindrome : ").lower()
PalinModifie = Palin.replace(" ","")
a = list(PalinModifie)


for i in range(0,len(a)//2):
    if a[i] == a[-(i+1)]:
        pass
    else:
        print("Ceci n'est pas un palindrome")
        break
print("Effectivement",Palin,"est un palindrome")