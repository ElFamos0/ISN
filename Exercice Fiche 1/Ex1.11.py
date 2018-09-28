# coding: utf-8
mot = input("Mettre une phrase")
phrase = input("Mettre un mot")
c = ""
for i in range(len(phrase)):
    c += phrase[i]+mot[i % len(mot)]

print(c)
