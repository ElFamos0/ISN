# coding: utf-8
import random
Lol  = input("Rentre un mot que ton amis doit deviner")
Motcherch = Lol.upper()
Mottrouve = ""
b = list(Motcherch)
random.shuffle(b)
for i in range(len(Motcherch)):
    Mottrouve += b[i]
print(Mottrouve)
v = "o"
while v.upper() !=  Motcherch:
    v = input("Quel est le mot original")
print("Bravo le mot était",Motcherch)
